'''
Screen to display summary statistics for match
'''

from GUI.inMatchScreen import *
from TennisMath.matchSimulation import *
from GUI.simulationScreen import *
from GUI.improveScreen import *
from GUI.startMatchScreen import *
from TennisMath.matchStatistics import *
from Class.playerClass import *

def findMatchOverButtons(event, data):
    for button in data.summaryStatsButtons:
        cx, cy, rw, ry = data.summaryStatsButtons[button]
        if event.x in range(cx - rw, cx + rw) and event.y in range(cy - ry, cy + ry):
            return button
    return None

def summaryStatsMousePressed(event, data):
    # if you click on the box then you can run the simulation
    if navClicked(event, data): return
    buttonPressed = findMatchOverButtons(event, data)
    if data.match.totalGamesMatch >= 3 and ((data.p1.gamesSet + data.p2.gamesSet) % 2 == 1 or
                                            data.p1.gamesSet + data.p2.gamesSet == 0):
        if buttonPressed == "Improve Game":
            data.p1.totalSimStats, data.p2.totalSimStats, data.p1.percMatchesWon, \
            data.p2.percMatchesWon = runSimulationLotsOfTimes(data)
            findWhatToImprove(data)
            data.mode = "simulation"
    if buttonPressed == "Play Match":
        data.changeover = False
        data.mode = "inMatch"

def summaryStatsKeyPressed(event, data):
    pass

def drawSummaryStats(canvas, data):
    if findYou(data)[0] == data.p1:
        p1Fill, p2Fill = data.accentColor, "black"
    else:
        p1Fill, p2Fill = "black", data.accentColor
    canvas.create_text(data.width//2, 30, text = "Match Statistics",
                       font = data.h2, fill = "white")
    canvas.create_rectangle(0, data.height//4 + 60, data.width, data.height,
                            fill = data.grayBackground, outline = data.grayBackground, width = 0)
    canvas.create_text(data.width//2 + data.buttonWidth - 125, data.height // 2 - 120,
                       anchor="center", text=str(data.p1.name), font=data.h3, fill=p1Fill)
    canvas.create_text(data.width//2 + data.buttonWidth - 50, data.height // 2 - 120,
                       anchor="center", text=str(data.p2.name), font=data.h3, fill=p2Fill)

    data.p1.findAveragePlayerStats()
    data.p2.findAveragePlayerStats()

    y, incY = data.height//2 - 115, 40
    canvas.create_text(data.width // 10 + 10, y - data.buttonHeight // 2,
                       anchor="nw", text="Serves", font=data.h3, fill="black")
    for i, label in enumerate(data.summaryStatsLabels):
        cx = data.width//2
        y += incY
        buffer = 10
        p1Stat, p2Stat = data.p1.averageStats[i], data.p2.averageStats[i]
        if i == 4:
            canvas.create_text(data.width//10 + buffer, y-data.buttonHeight//2,
                               anchor = "nw", text = "Returns", font = data.h3, fill = "black")
            y += incY
        canvas.create_rectangle(cx - data.buttonWidth, y - data.buttonHeight,
                                cx + data.buttonWidth, y + data.buttonHeight,
                                outline = data.grayBackground, width = 1, fill = "white") # white background rectangle
        canvas.create_text(data.width // 10 + buffer, y-data.buttonHeight//2,
                           anchor="nw", text= label, font=data.h3, fill="black") # labels
        canvas.create_text(cx + data.buttonWidth - 125, y, anchor="center",
                           text=str(round(p1Stat * 100, 2)) + "%", font=data.h3, fill=p1Fill) # p1Stat
        canvas.create_text(cx + data.buttonWidth - 50, y, anchor="center",
                           text=str(round(p2Stat * 100, 2)) + "%", font=data.h3, fill=p2Fill) # p2Stat

    canvas.create_line(data.width//2 + data.buttonWidth-87, data.height//2-120,
                       data.width//2 + data.buttonWidth-87, data.height,
                       fill = data.grayBackground, width = 1)


def drawSimulationButton(canvas, data):
    for button in data.summaryStatsButtons:
        cx, cy, rw, ry = data.summaryStatsButtons[button]
        canvas.create_rectangle(cx-rw, cy-ry, cx+rw, cy+ry, fill = data.accentColor,
                                outline = data.accentColor, width = 0, activefill = data.accentColor2)
        canvas.create_text(cx, cy, text = button, anchor = "center",
                           font = data.h3, fill = "white")


def summaryStatsRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.inMatchScreenBackground)
    drawMatchSummary(canvas, data)
    drawSummaryStats(canvas, data)
    drawSimulationButton(canvas, data)
    drawNavigation(canvas, data)


