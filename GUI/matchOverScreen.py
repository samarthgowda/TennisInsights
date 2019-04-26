# match over screen
from GUI.loginScreen import *
from GUI.inMatchScreen import *
import os
import math

def resetMatch(data):
    data.currentSet = 1
    for button in data.startMatchButtons:
        data.startMatchButtons[button][5] = False
    try:
        del data.p1
        del data.p2
        del data.match
    except:
        return None

def findMatchOverButtons(event, data):
    for button in data.matchOverButtons:
        cx, cy, rw, ry = data.matchOverButtons[button]
        if event.x in range(cx - rw, cx + rw) and event.y in range(cy - ry, cy + ry):
            return button
    return None

def matchOverMousePressed(event, data):
    buttonPressed = findMatchOverButtons(event, data)
    if buttonPressed == "Home":
        saveMatchInfo(data)
        resetMatch(data)
        data.mode = "home"
    if buttonPressed == "Match Summary":
        data.mode = "summaryStats"
    if buttonPressed == "Log Out":
        saveMatchInfo(data)
        resetMatch(data)
        logOut()
        data.mode = "login"

def logOut():
    if os.path.isfile("token.json"):
        os.remove("token.json")

def matchOverKeyPressed(event, data):
    if event.keysym == "s":
        data.mode = "summaryStats"

def matchOverRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw",
                        image = data.matchOverScreenBackground)
    canvas.create_text(40, data.height//2 - 50,
                       anchor="nw", fill="white", text=data.p1.name, font=data.h1)
    canvas.create_text(40, data.height//2,
                       anchor="nw", fill="white", text=data.p2.name, font=data.h1)
    x, incX = data.width//4 + 20, 46
    for score in data.p1.setScores:
        x += incX
        canvas.create_text(x, data.height//2 - 50,
                           anchor="nw", fill="white", text=str(score), font=data.h1)
    x, incX = data.width//4 + 20, 46
    for score in data.p2.setScores:
        x += incX
        canvas.create_text(x, data.height//2,
                           anchor="nw", fill="white", text=str(score), font=data.h1)
    for button in data.matchOverButtons:
        cx, cy, rw, ry = data.matchOverButtons[button]
        canvas.create_rectangle(cx-rw, cy-ry, cx+rw, cy+ry,
                                outline = "white", width = 0,
                                fill = data.mainColor, activefill = data.accentMainColor)
        canvas.create_text(cx, cy, text = button,
                           anchor = "center", font = data.h3, fill = "white")


def saveMatchInfo(data):
    you, opponent = findYou(data)[0], findYou(data)[1]
    if max(you.setsMatch, opponent.setsMatch) == math.ceil(data.match.totalNumSets/2):
        # finds out who won the match if the match ended
        if you.setsMatch > opponent.setsMatch:
            data.winning = True
        else:
            data.winning = False

    you.findAveragePlayerStats() # finds the average player stats for the match
    avgStats = you.averageStats
    d = readFile("users/"+data.email+".json")
    for i, stat in enumerate(avgStats): # add the stats to the json file
        label = data.summaryStatsLabels[i]
        statLst = d.get(label, [])
        statLst.append(stat)
        d[label] = statLst
    dateLst = d.get("date", [])
    dateLst.append(data.date)
    d["date"] = dateLst
    if data.winning:
        recordLst = d.get("record", [])
        recordLst.append(1)
        d["record"] = recordLst
    else:
        recordLst = d.get("record", [])
        recordLst.append(0)
        d["record"] = recordLst

    writeFile("users/"+data.email+".json", d)

    data.playerInfoDict = readFile("users/" + data.email + ".json")




