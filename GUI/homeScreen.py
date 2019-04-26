'''
Home Screen Gui
'''

from GUI.matchOverScreen import *
from GUI.startMatchScreen import *
from GUI.matchOverScreen import *
from GUI.matchHistoryGraphs import *

def startButton():
    print("hello")

def isMatchHistoryLegal(data):
    d = data.playerInfoDict
    try:
        if len(d["record"]) > 1:
            return True
    except:
        return False

def homeMousePressed(event, data):
    if navClicked(event, data): return
    for button in data.homeButtons:
        cx, cy, rw, ry, command = data.homeButtons[button]
        if event.x in range(cx-rw, cx+rw) and event.y in range(cy-ry, cy+ry):
            if button == "Start Match":
                resetMatch(data)
                data.mode = "startMatch"
            if button == "Match History" and isMatchHistoryLegal(data):
                drawGraphs(data)
                data.mode = "matchHistory"
                break
            if button == "Log Out":
                logOut()
                data.mode = "login"
                break
            if button == "Help":
                data.mode = "help"

def homeKeyPressed(event, data):
    if event.keysym == "s":
        resetMatch(data)
        data.mode = "startMatch"
    if event.keysym == "h":
        data.mode = "help"


def homeRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.homeScreenBackground)
    for button in data.homeButtons:
        cx, cy, rw, ry, command = data.homeButtons[button]
        canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                outline="white", width=0, fill=data.accentColor, activefill=data.accentColor2)
        canvas.create_text(cx, cy, text=button, anchor="center", font=data.h3, fill="white")
    drawNavigation(canvas, data)



