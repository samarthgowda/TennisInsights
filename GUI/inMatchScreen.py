'''
Screen for in Match Gui
'''
from TennisMath.matchStatistics import *
from GUI.startMatchScreen import *

def findYou(data):
    if data.p1.name == "You":
        return (data.p1, data.p2)
    else:
        return (data.p2, data.p1)

def findMatchButtonPress(event, data):
    for button in data.inMatchNavButtons:
        cx, cy, rw, ry = data.inMatchNavButtons[button]
        if event.x in range(cx - rw, cx + rw) and event.y in range(cy - ry, cy + ry):
            return button

    for button in data.inMatchButtons:
        cx, cy, rw, ry, clicked = data.inMatchButtons[button]
        if event.x in range(cx-rw, cx+rw) and event.y in range(cy-ry, cy+ry):
            data.inMatchButtons[button][4] = not data.inMatchButtons[button][4]
            return button
    return None

def findClickedButtons(data):
    result = set()
    for button in data.inMatchButtons:
        clicked = data.inMatchButtons[button][4]
        if clicked:
            result.add(button)
    return result

def removeClickFromButtons(data):
    for button in data.inMatchButtons:
        clicked = data.inMatchButtons[button][4]
        if clicked:
            data.inMatchButtons[button][4] = False

def checkInMatchClicked(data):
    group = {1:("1st Serve In", "2nd Serve In", "Double Fault"), 2:("In", "Out")}
    clickedLst = []
    for button in data.inMatchButtons:
        clicked = data.inMatchButtons[button][4]
        if clicked:
            clickedLst.append(button)
    if "Double Fault" in clickedLst:
        if len(clickedLst) == 2:
            return True
        return False
    for key in group:
        count = 0
        for value in group[key]:
            if value in clickedLst:
                count += 1
        if count is not 1:
            return False
    return True

def updateMatchStats(data, buttonPressed):
    clickedButtons = findClickedButtons(data)
    you, opponent = findYou(data)[0], findYou(data)[1]
    if data.serving:
        server, returner = you, opponent
    else:
        server, returner = opponent, you

    if buttonPressed == "Won" and checkInMatchClicked(data):
        if "1st Serve In" in clickedButtons:
            server.firstServeMade(True) # server made first serve in
            if data.serving:
                you.firstServePointWon(True) # you won first serve point
                opponent.firstServeReturnWon(False)
            else:
                opponent.firstServePointWon(False) # opponent lost first serve point
                you.firstServeReturnWon(True)
            if "In" in clickedButtons:
                returner.firstReturnMade(True) # returner made first serve return
            elif "Out" in clickedButtons:
                returner.firstReturnMade(False) # returner missed first serve return
        elif "2nd Serve In" in clickedButtons:
            server.firstServeMade(False) # server missed first serve
            server.secondServeMade(True) # server made second serve
            if data.serving:
                you.secondServePointWon(True) # you won second serve point
                opponent.secondServeReturnWon(False)
            else:
                opponent.secondServePointWon(False) # opponent lost second serve point
                you.secondServeReturnWon(True)
            if "In" in clickedButtons:
                returner.secondReturnMade(True) # returner made second serve return
            elif "Out" in clickedButtons:
                returner.secondReturnMade(False) # returner missed second serve return
        elif "Double Fault" in clickedButtons:
            server.firstServeMade(False) # server missed first serve
            server.secondServeMade(False) # server missed second serve
        # incrementing the points in game/tiebreak accordingly
        if not data.tiebreaker:
            you.pointsGame += 1
            updateSet(data)
        else:
            you.pointsTie += 1
            updateSet(data)
        you.pointsMatch += 1
        removeClickFromButtons(data)

    elif buttonPressed == "Lost" and checkInMatchClicked(data):
        if "1st Serve In" in clickedButtons:
            server.firstServeMade(True) # server made first serve in
            if data.serving:
                you.firstServePointWon(False) # you lost first serve point
                opponent.firstServeReturnWon(True)
            else:
                opponent.firstServePointWon(True) # opponent won first serve point
                you.firstServeReturnWon(False)
            if "In" in clickedButtons:
                returner.firstReturnMade(True) # returner made first serve return
            elif "Out" in clickedButtons:
                returner.firstReturnMade(False) # returner missed first serve return
        elif "2nd Serve In" in clickedButtons:
            server.firstServeMade(False) # server missed first serve
            server.secondServeMade(True) # server made second serve
            if data.serving:
                you.secondServePointWon(False) # you lost second serve point
                opponent.secondServeReturnWon(True)
            else:
                opponent.secondServePointWon(True) # opponent won second serve point
                you.secondServeReturnWon(False)
            if "In" in clickedButtons:
                returner.secondReturnMade(True) # returner made second serve return
            elif "Out" in clickedButtons:
                returner.secondReturnMade(False) # returner missed second serve return
        elif "Double Fault" in clickedButtons:
            server.firstServeMade(False) # server missed first serve
            server.firstServeMade(True) # server missed second serve
        # incrementing the points in game/tiebreak accordingly
        if not data.tiebreaker:
            opponent.pointsGame += 1
            updateSet(data)
        else:
            opponent.pointsTie += 1
            updateSet(data)
        opponent.pointsMatch +=1
        removeClickFromButtons(data)
    data.p1.findAveragePlayerStats()
    data.p2.findAveragePlayerStats()



def inMatchMousePressed(event, data):
    if navClicked(event, data): return
    buttonPressed = findMatchButtonPress(event, data)
    if buttonPressed == "Match Stats":
        data.mode = "summaryStats"
        return
    if buttonPressed == "End Game":
        data.mode = "matchOver"
        return
    updateMatchStats(data, buttonPressed)
    # checkForChangeover(data)

def checkForChangeover(data):
    if (data.p1.gamesSet + data.p2.gamesSet) % 2 == 1:
        data.changeover = True
        if data.changeover:
            data.mode = "summaryStats"

def inMatchKeyPressed(event, data):
    if event.keysym == "g":
        data.mode = "matchOver"
    if event.keysym == "s":
        data.mode = "summaryStats"

def inMatchRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.inMatchScreenBackground)
    canvas.create_text(data.width//2, 30, text = "Live Match", font = data.h2, fill = "white")
    if data.serving: gameStatus = "Serving"
    else: gameStatus = "Returning"
    print("drawPlayGame is called")
    # serving/returning bar
    canvas.create_rectangle(0, data.height//4, data.width,
                            data.height//4+60, outline=data.accentMainColor,
                            width = 0, fill = data.accentMainColor)
    canvas.create_text(data.width//2, data.height//4+30, text = gameStatus,
                       fill = data.accentColor, font = data.h1)

    drawMatchSummary(canvas, data)
    drawPlayGame(canvas, data)
    drawPlayButtons(canvas, data)
    drawNavButtons(canvas, data)
    drawNavigation(canvas, data)

def drawMatchSummary(canvas, data):
    canvas.create_text(25, 75, anchor="nw", fill="white",
                       text=data.p1.name, font=data.h1)
    canvas.create_text(25, 130, anchor="nw", fill="white",
                       text=data.p2.name, font=data.h1)
    x, incX = 231, 46
    for i, score in enumerate(data.p1.setScores):
        x += incX
        canvas.create_text(x, 75, anchor="nw", fill="white",
                           text=str(score), font=data.h1)
        canvas.create_text(x, 50, anchor = "nw", fill = "white",
                           text = str(i+1), font = data.h3) # set number above score
    x, incX = 231, 46
    for score in data.p2.setScores:
        x += incX
        canvas.create_text(x, 130, anchor="nw", fill="white",
                           text=str(score), font=data.h1)

    if not data.tiebreaker:
        scoreTextP1 = findGameDisplayScore(data, data.p1.pointsGame, data.p2.pointsGame)
        scoreTextP2 = findGameDisplayScore(data, data.p2.pointsGame, data.p1.pointsGame)
    else:
        scoreTextP1, scoreTextP2 = data.p1.pointsTie, data.p2.pointsTie
    canvas.create_text(226, 90, anchor="center", fill=data.accentColor,
                       text=str(scoreTextP1), font=data.h1)
    canvas.create_text(226, 145, anchor="center", fill=data.accentColor,
                       text=str(scoreTextP2), font=data.h1)

def drawPlayGame(canvas, data):
    canvas.create_rectangle(0, data.height//4 + 60, data.width, data.height,
                            fill = data.grayBackground, outline = data.grayBackground, width = 0)
    canvas.create_text(data.width//10, data.height//4 + 80, anchor = "nw",
                       text = "Serve Result", fill = "black", font = data.h3)
    canvas.create_text(data.width//10, data.height//2 + 40, anchor = "nw",
                       text = "Return Result", fill = "black", font = data.h3)
    canvas.create_text(data.width//10, 80+data.height//2 + 4*data.buttonHeight,
                       anchor = "nw", text = "Point Result", fill = "black", font = data.h3)

def createInMatchButtons(data):
    d = dict()
    lst = ["1st Serve In", "2nd Serve In", "Double Fault", "In", "Out", "Won", "Lost"]
    cx = data.width//2
    bWidth, bHeight = data.buttonWidth, data.buttonHeight
    clicked = False
    startHeight, buffer, z = data.height//4, 130, -2
    for i, button in enumerate(lst):
        z += 2
        if i == 3 or i == 5: z += 2
        cy = buffer + startHeight + bHeight*z
        d[button] = [cx, cy, bWidth, bHeight, clicked]
    return d

def drawPlayButtons(canvas, data):
    # draw buttons for inMatchScreen
    for i, button in enumerate(data.inMatchButtons):
        cx, cy, rw, ry, clicked = data.inMatchButtons[button]
        if clicked:
            canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                    outline = data.accentColor, width = 0, fill=data.accentColor)
            canvas.create_text(data.width//10 + 20, cy - ry//4, text=button,
                               anchor="nw", font=data.h3, fill="white")
        else:
            canvas.create_rectangle(cx-rw, cy-ry, cx+rw, cy+ry, outline = data.grayBackground,
                                    width = 1, fill = "white", activefill = data.accentColor)
            canvas.create_text(data.width//10 + 20, cy - ry//4, text = button,
                               anchor = "nw", font = data.h3, fill = "black")

def drawNavButtons(canvas, data):
    for i, button in enumerate(data.inMatchNavButtons):
        cx, cy, rw, ry = data.inMatchNavButtons[button]
        canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry, fill=data.accentColor,
                                outline=data.accentColor, width=0, activefill = data.accentColor2)
        canvas.create_text(cx, cy, text=button, anchor="center", font=data.h3, fill="white")
