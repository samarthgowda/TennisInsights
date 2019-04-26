# match history screen
from GUI.startMatchScreen import *
import os
from tkinter import *
from GUI.matchHistoryGraphs import *
from GUI.startMatchScreen import *


def matchHistoryMousePressed(event, data):
    if navClicked(event, data): return
    for button in data.matchHistoryButtons:
        cx, cy, rw, ry, clicked = data.matchHistoryButtons[button]
        data.matchHistoryButtons[button][4] = False
        if event.x in range(cx-rw, cx+rw) and event.y in range(cy-ry, cy+ry):
            data.matchHistoryButtons[button][4] = True
            data.currentGraph = button
            drawGraphs(data)

def matchHistoryKeyPressed(event, data):
    if event.keysym == "h":
        data.mode = "home"

def matchHistoryRedrawAll(canvas, data):
    buttonTxtLst = ["1st Serve In", "2nd Serve In", "1st Serve \nPoints Won",
                    "2nd Serve \nPoints Won","1st Serve \nReturns In", "2nd Serve \nReturns In",
                    "1st Serve \nReturn Won", "2nd Serve \nReturn Won"]
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "white")
    canvas.create_text(data.width//2, 30, text = "Match History",
                       font = data.h2, fill = "black")
    canvas.create_text(data.width//2, 75, text = "Welcome " + data.name + "!",
                       font = data.h2, fill = "black")
    baseFolder = os.path.dirname(os.path.dirname(__file__))
    currentGraphPath = os.path.join(baseFolder, 'graphs' + os.sep +
                                    data.currentGraph + '.png')
    data.currentGraphImg = PhotoImage(file=currentGraphPath,
                                      width=448, height=336)
    canvas.create_image(data.width // 2, data.height // 2 + 50,
                        anchor="center", image=data.currentGraphImg)
    drawNavigation(canvas, data)
    wins, losses = data.playerInfoDict["record"].count(1), \
                   data.playerInfoDict["record"].count(0)
    canvas.create_text(data.width//2, 125, text = "Record: " + str(wins) + "-" + str(losses),
                       font = data.h1Large, fill = data.accentColor)
    for i, button in enumerate(data.matchHistoryButtons):
        cx, cy, rw, ry, clicked = data.matchHistoryButtons[button]
        txt = buttonTxtLst[i]
        if clicked:
            canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                    outline="white", width=0, fill=data.grayBackground)
            canvas.create_text(cx, cy, text=txt, anchor="center", font=data.h3, fill="black")
        else:
            canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                    outline="white", width=0, fill="white", activefill=data.grayBackground)
            canvas.create_text(cx, cy, text=txt, anchor="center",
                               font=data.h3, fill="black")




