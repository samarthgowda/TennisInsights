'''
Screen to display the simulation running
'''

from TennisMath.matchSimulation import *
from GUI.inMatchScreen import *
from GUI.improveScreen import *
from GUI.startMatchScreen import *


def findSimulationButtons(event, data):
    for button in data.simulationButtons:
        cx, cy, rw, ry = data.simulationButtons[button]
        if event.x in range(cx - rw, cx + rw) and event.y in range(cy - ry, cy + ry):
            return button
    return None

def simulationMousePressed(event, data):
    if navClicked(event, data): return
    buttonPressed = findSimulationButtons(event, data)
    if buttonPressed == "Play Match":
        data.mode = "inMatch"
    elif buttonPressed == "Improve Game":
        data.mode = "improve"

def simulationKeyPressed(event, data):
    if event.keysym == "i":
        data.mode = "improve"


def simulationRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.inMatchScreenBackground)
    canvas.create_text(data.width//2, 30, text = "Simulation", font = data.h2, fill = "white")
    drawMatchSummary(canvas, data)
    if findYou(data)[0] == data.p1:
        simStats = data.p1.totalSimStats
        percMatchesWon = data.p1.percMatchesWon
        averageStats = data.p1.averageStats
    if findYou(data)[0] == data.p2:
        simStats = data.p2.totalSimStats
        percMatchesWon = data.p2.percMatchesWon
        averageStats = data.p2.averageStats

    if percMatchesWon > 50:
        data.winning = True
    else:
        data.winning = False

    canvas.create_rectangle(0, data.height // 4 + 60, data.width, data.height,
                            fill=data.grayBackground, outline=data.grayBackground, width=0)
    canvas.create_text(data.width//2, data.height // 2 - 115,
                       text = "You have a " + str(round(percMatchesWon, 2)) + "% chance of winning.",
                       font = data.h3, fill = "black")
    canvas.create_text(data.width // 2 + data.buttonWidth - 125,
                       data.height // 2 - 80, anchor="center", text="Current", font=data.h3,
                       fill="black")
    canvas.create_text(data.width // 2 + data.buttonWidth - 50,
                       data.height // 2 - 80, anchor="center", text="Aim", font=data.h3,
                       fill=data.accentColor)

    y, incY = data.height // 2 - 75, 40
    canvas.create_text(data.width // 10 + 10, y - data.buttonHeight // 2,
                       anchor="nw", text="Serves", font=data.h3, fill="black")
    for i, label in enumerate(data.summaryStatsLabels):
        cx = data.width // 2
        y += incY
        buffer = 10
        avgStat, simStat = averageStats[i], simStats[i]
        if i == 4:
            canvas.create_text(data.width // 10 + buffer, y - data.buttonHeight // 2,
                               anchor="nw", text="Returns", font=data.h3, fill="black")
            y += incY
        canvas.create_rectangle(cx - data.buttonWidth, y - data.buttonHeight,
                                cx + data.buttonWidth, y + data.buttonHeight,
                                outline=data.grayBackground, width=1, fill="white")  # white background rectangle
        canvas.create_text(data.width // 10 + buffer, y - data.buttonHeight // 2,
                           anchor="nw", text=label, font=data.h3, fill="black")  # labels
        canvas.create_text(cx + data.buttonWidth - 125, y, anchor="center",
                           text=str(round(avgStat * 100, 2)) + "%", font=data.h3,
                           fill="black")  # avgStat
        canvas.create_text(cx + data.buttonWidth - 50, y, anchor="center",
                           text=str(round(simStat * 100, 2)) + "%", font=data.h3,
                           fill= data.accentColor)  # simStat

    canvas.create_line(data.width // 2 + data.buttonWidth - 87, data.height // 2 - 120,
                       data.width // 2 + data.buttonWidth - 87, data.height,
                       fill=data.grayBackground, width=1)

    for button in data.simulationButtons:
            cx, cy, rw, ry = data.simulationButtons[button]
            canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry,
                                    fill=data.accentColor, outline=data.accentColor,
                                    width=0, activefill = data.accentColor2)
            canvas.create_text(cx, cy, text=button, anchor="center", font=data.h3, fill="white")

    drawNavigation(canvas, data)


