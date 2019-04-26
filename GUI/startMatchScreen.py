'''
Screen to take user inputs before starting the match
'''
from Class.playerClass import *
from Class.matchClass import *
from TennisMath.matchStatistics import *
from GUI.matchOverScreen import *


def findButtonPress(event, data):
    for button in data.startMatchButtons:
        cx, cy, rw, ry, command, clicked = data.startMatchButtons[button]
        if event.x in range(cx-rw, cx+rw) and event.y in range(cy-ry, cy+ry):
            data.startMatchButtons[button][5] = not data.startMatchButtons[button][5]
            return button
    return None

def checkStartMatchClicked(data):
    group = {1:("3", "5"), 2:("Serve", "Return")}
    clickedLst = []
    for button in data.startMatchButtons:
        clicked = data.startMatchButtons[button][5]
        if clicked:
            clickedLst.append(button)
    for key in group:
        count = 0
        for value in group[key]:
            if value in clickedLst:
                count += 1
        if count is not 1:
            return False
    return True


def startMatchMousePressed(event, data):
    if navClicked(event, data): return
    findButtonPress(event, data)
    for button in data.startMatchButtons:
        clicked = data.startMatchButtons[button][5]
        if clicked:
            if button == "3":
                data.totalNumSets = 3
            if button == "5":
                data.totalNumSets = 5
            if button == "Serve":
                data.p1Name, data.p2Name = "You", "Opponent"
            if button == "Return":
                data.p1Name, data.p2Name = "Opponent", "You"
            if button == "Start" and checkStartMatchClicked(data):
                data.p1, data.p2 = createPlayers(data)
                data.match = createMatch(data)
                data.p1.stats = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0], [1,1,1,1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,]] #nadal

                data.p2.stats = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                                [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]] #federer
                data.p1.gamesSet, data.p2.gamesSet = 4, 2
                data.match.totalGamesMatch = data.p1.gamesSet + data.p2.gamesSet
                updateSet(data)
                data.mode = "inMatch"


def createPlayers(data):
    p1 = Player(data.p1Name)
    p2 = Player(data.p2Name)
    return p1, p2

def createMatch(data):
    return Match(data.totalNumSets, data.p1, data.p2)

def startMatchKeyPressed(event, data):
    if event.keysym == "g":
        data.mode = "inMatch"
    if event.keysym == "h":
        data.mode = "home"


def startMatchRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill = data.mainColor)
    canvas.create_text(data.width//2, 30, text = "Match Setup", font = data.h2, fill = "white")
    canvas.create_text(data.width//2, data.height//4 - 90,
                       text = "Welcome " + data.name + "!", font = data.h1, fill = "white")
    count = 0
    for button in data.startMatchButtons:
        count += 1
        if count == 5: size = data.h1
        else: size = data.h1Large
        cx, cy, rw, ry, command, clicked = data.startMatchButtons[button]
        if clicked:
            canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                    outline = data.accentColor, width = 0, fill=data.accentColor)
            canvas.create_text(cx, cy - 5, text=button, anchor="center", font=size, fill="white")
        else:
            canvas.create_rectangle(cx-rw, cy-ry, cx+rw, cy+ry, fill = "#d9d9d9",
                                    outline = "#d9d9d9", width = 0, activefill = data.accentColor)
            canvas.create_text(cx, cy - 5, text = button, anchor = "center", font = size, fill = "white")


    for text in data.startMatchText:
        cx, cy = data.startMatchText[text]
        canvas.create_text(cx - data.width//4, cy, text = text, anchor = "center", fill = "white", font = data.h3)
        canvas.create_text(cx + data.width//4, cy, text = text, anchor = "center", fill = "white", font = data.h3)

    drawNavigation(canvas, data)

def drawNavigation(canvas, data):
    canvas.create_rectangle(0, data.height - 50, data.width, data.height, fill="white", outline="white",width=0)
    for i, button in enumerate(data.navButtons):
        cx, cy, rw, ry, clicked = data.navButtons[button]
        if data.mode == button:
            clicked = True
        canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry, fill="white",
                                activefill=data.grayBackground, outline = "white", width = 0)
        if clicked:
            img = data.navImagesClicked[i]
            canvas.create_image(cx, cy, anchor="center", image=img)
        if not clicked:
            img = data.navImages[i]
            canvas.create_image(cx, cy, anchor="center", image=img)
def resetNavButtons(data):
    for button in data.navButtons:
        data.navButtons[button][4] = False

def navClicked(event, data):
    resetNavButtons(data)
    for button in data.navButtons:
        cx, cy, rw, ry, clicked = data.navButtons[button]
        try:
            if data.match.totalGamesMatch == 0 and \
                    data.p1.pointsGame == 0 and data.p2.pointsGame == 0: match = False
            else: match = True
        except:
            match = False
        if event.x in range(cx - rw, cx + rw) and event.y in range(cy - ry, cy + ry):

            if button == "home":
                data.mode = button
                data.navButtons[button][4] = True
            elif button == "inMatch" and (data.mode == "summaryStats" or
                data.mode == "simulation" or data.mode == "improve") or \
                    ((data.mode == "help" or data.mode == "home") and match):
                data.mode = button
                data.navButtons[button][4] = True

            elif button == "summaryStats" and (data.mode == "inMatch" or
                data.mode == "simulation" or data.mode == "improve" or
                data.mode == "matchOver" or ((data.mode == "help" or data.mode == "home") and match)):
                data.mode = button
                data.navButtons[button][4] = True

            elif button == "help":
                data.mode = button
                data.navButtons[button][4] = True

            return True
