'''
Screen to display the recommendation to the players after running the simulation
'''
from GUI.inMatchScreen import *
from GUI.startMatchScreen import *


def findImproveButtons(event, data):
    for button in data.improveButtons:
        cx, cy, rw, ry = data.improveButtons[button]
        if event.x in range(cx - rw, cx + rw) and event.y in range(cy - ry, cy + ry):
            return button
    return None

def findWhatToImprove(data): # find top 3 things to improve on
    if findYou(data)[0] == data.p1:
        you = data.p1
        simStats = data.p1.totalSimStats
        averageStats = data.p1.averageStats
    if findYou(data)[0] == data.p2:
        you = data.p2
        simStats = data.p2.totalSimStats
        averageStats = data.p2.averageStats
    print(simStats)
    print(averageStats)
    you.improve = []

    for i, stats in enumerate(simStats):
        value = simStats[i] - averageStats[i]
        you.improve.append((value, i))

    you.improve = sorted(you.improve, reverse=True)[:5]


def improveMousePressed(event, data):
    if navClicked(event, data): return
    buttonPressed = findImproveButtons(event, data)
    if buttonPressed == "Play Match":
        data.mode = "inMatch"
    elif buttonPressed == "Simulation":
        data.mode = "simulation"


def improveKeyPressed(event, data):
    if event.keysym == "s":
        data.mode = "simulation"

def improveRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.inMatchScreenBackground)
    drawMatchSummary(canvas, data)
    canvas.create_text(data.width//2, 30, text = "Improve", font = data.h2, fill = "white")
    you = findYou(data)[0]
    # simulation stats

    canvas.create_rectangle(0, data.height // 4 + 60, data.width, data.height,
                            fill=data.grayBackground, outline=data.grayBackground, width=0)
    canvas.create_text(data.width // 2 + data.buttonWidth - 125, data.height // 2 - 80,
                       anchor="center", text="Current", font=data.h3,
                       fill="black")
    canvas.create_text(data.width // 2 + data.buttonWidth - 50, data.height // 2 - 80,
                       anchor="center", text="Amount", font=data.h3,
                       fill=data.accentColor)

    y, incY = data.height // 2 - 75, 40
    canvas.create_text(data.width // 10 + 10, y - data.buttonHeight // 2, anchor="nw",
                       text="Increase", font=data.h3, fill="black")
    for i, stat in enumerate(you.improve):
        cx = data.width // 2
        y += incY
        buffer = 10
        value, z, avgStat = stat[0], stat[1], you.averageStats[i]
        canvas.create_rectangle(cx - data.buttonWidth, y - data.buttonHeight,
                                cx + data.buttonWidth, y + data.buttonHeight,
                                outline=data.grayBackground, width=1, fill="white")  # white background rectangle
        canvas.create_text(data.width // 10 + buffer, y - data.buttonHeight // 2,
                           anchor="nw", text=data.summaryStatsLabels[z], font=data.h3, fill="black")  # labels
        canvas.create_text(cx + data.buttonWidth - 125, y, anchor="center",
                           text=str(round(avgStat * 100, 2)) + "%", font=data.h3,
                           fill="black")  # avgStat
        canvas.create_text(cx + data.buttonWidth - 50, y, anchor="center",
                           text="+ " + str(round(value * 100, 2)) + "%", font=data.h3,
                           fill=data.accentColor)  # amount

    canvas.create_line(data.width // 2 + data.buttonWidth - 87, data.height // 2 - 120,
                       data.width // 2 + data.buttonWidth - 87, data.height,
                       fill=data.grayBackground, width=1)

    for button in data.improveButtons:
        cx, cy, rw, ry = data.improveButtons[button]
        canvas.create_rectangle(cx - rw, cy - ry, cx + rw, cy + ry, fill=data.accentColor,
                                outline=data.accentColor, width=0, activefill = data.accentColor2)
        canvas.create_text(cx, cy, text=button, anchor="center", font=data.h3, fill="white")

    drawNavigation(canvas, data)

