'''
Citation: Mode Demo Template from 15-112 Course Notes https://www.cs.cmu.edu/~112/notes/notes-animations-demos.html
'''

from tkinter import *
import os

# main gui file that will have initial data values
# as well as mode dispatcher and run function for tkinter

from GUI.homeScreen import *
from GUI.helpScreen import *
from GUI.startMatchScreen import *
from GUI.inMatchScreen import *
from GUI.summaryStatsScreen import *
from GUI.simulationScreen import *
from GUI.improveScreen import *
from GUI.matchOverScreen import *
from GUI.matchHistory import *
from GUI.loginScreen import *
import datetime
# import Player Class


####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "login"
    now = datetime.datetime.now()
    data.date = str(now.month) + "-" + str(now.day) + "-" + str(now.year)
    baseFolder = os.path.dirname(os.path.dirname(__file__))
    googlePlusPath = os.path.join(baseFolder, 'Images' + os.sep + 'googleplus.png')
    data.googlePlusImg = PhotoImage(file=googlePlusPath, width=50, height=50)
    # background images
    homeScreenBackgroundPath = os.path.join(baseFolder, 'Images' + os.sep + 'homeScreenBackground.png')
    matchScreenBackgroundPath = os.path.join(baseFolder, 'Images' + os.sep + 'inMatchScreenBackground.png')
    matchOverScreenBackgroundPath = os.path.join(baseFolder, 'Images' + os.sep + 'matchOverScreenBackground.png')
    helpScreenBackgroundPath = os.path.join(baseFolder, 'Images' + os.sep + 'helpScreenBackground.png')
    data.homeScreenBackground = PhotoImage(file=homeScreenBackgroundPath, width=500, height=800)
    data.inMatchScreenBackground = PhotoImage(file=matchScreenBackgroundPath, width=500, height=800)
    data.matchOverScreenBackground = PhotoImage(file=matchOverScreenBackgroundPath, width=500, height=800)
    data.helpScreenBackground = PhotoImage(file=helpScreenBackgroundPath, width=500, height=800)
    # nav images
    homeNavPath = os.path.join(baseFolder, 'Images' + os.sep + 'home.png')
    matchNavPath = os.path.join(baseFolder, 'Images' + os.sep + 'match.png')
    statNavPath = os.path.join(baseFolder, 'Images' + os.sep + 'stats.png')
    helpNavPath = os.path.join(baseFolder, 'Images' + os.sep + 'help.png')
    homeNavPathClicked = os.path.join(baseFolder, 'Images' + os.sep + 'homeClicked.png')
    matchNavPathClicked = os.path.join(baseFolder, 'Images' + os.sep + 'matchClicked.png')
    statNavPathClicked = os.path.join(baseFolder, 'Images' + os.sep + 'statsClicked.png')
    helpNavPathClicked = os.path.join(baseFolder, 'Images' + os.sep + 'helpClicked.png')
    data.homeNavImg = PhotoImage(file=homeNavPath, width=40, height=40)
    data.matchNavImg = PhotoImage(file=matchNavPath, width=40, height=40)
    data.statNavImg = PhotoImage(file=statNavPath, width=40, height=40)
    data.helpNavImg = PhotoImage(file=helpNavPath, width=40, height=40)
    data.homeNavImgClicked = PhotoImage(file=homeNavPathClicked, width=40, height=40)
    data.matchNavImgClicked = PhotoImage(file=matchNavPathClicked, width=40, height=40)
    data.statNavImgClicked = PhotoImage(file=statNavPathClicked, width=40, height=40)
    data.helpNavImgClicked = PhotoImage(file=helpNavPathClicked, width=40, height=40)

    data.navImages = [data.homeNavImg, data.matchNavImg, data.statNavImg, data.helpNavImg]
    data.navImagesClicked = [data.homeNavImgClicked, data.matchNavImgClicked, data.statNavImgClicked, data.helpNavImgClicked]

    data.h1Large, data.h1, data.h2, data.h3 = "OpenSans 60","OpenSans 22", "OpenSans 20", "OpenSans 14"
    data.mainColor, data.accentMainColor, data.accentColor, \
    data.accentColor2, data.grayBackground = "#1a284b", "#0d1d44", "#eb1239", "#fa1b43", "#f3f3f4"
    data.buttonWidth, data.buttonHeight = data.width//2 - data.width//10, 20
    data.navButtons = {
        "home": [data.width//5, data.height-25, data.width//10, 25, True],
        "inMatch": [2*data.width//5, data.height-25, data.width//10, 25, False],
        "summaryStats": [3*data.width//5, data.height-25, data.width//10, 25, False],
        "help": [4*data.width//5, data.height-25, data.width//10, 25, False]
    }
    data.loginButtons = {"Sign in with Google+": [data.width//2, data.height//2 + 25, 125, 25]}

    data.homeButtons = {"Start Match": [data.width // 2, data.height // 2 + 25, 125, 25, "startMatch"],
                        "Help": [data.width // 2 - 65, data.height // 2 + 145, 60, 25, "help"],
                        "Log Out": [data.width // 2 + 65, data.height // 2 + 145, 60, 25, "logOut"],
                        "Match History": [data.width // 2, data.height // 2 + 85, 125, 25, "matchHistory"]}

    data.startMatchButtons = {"3": [data.width//4, data.height//4, data.width//4, 60, 3, False],
                              "5": [3*data.width//4, data.height//4, data.width//4, 60, 5, False],
                              "Serve": [data.width//4, data.height//4 + 120, data.width//4, 60, "p1", False],
                              "Return": [3*data.width//4, data.height//4 + 120, data.width//4, 60, "p1", False],
                              "Start": [data.width//2, data.height//4 + 210, data.width//2, 30, "inMatch", False]
    }
    data.startMatchText = {
        "Sets": [data.width//2, data.height//4 + 40],
        "First": [data.width//2, data.height//4 + 160]
    }
    data.tennisGameScoring = [0, 15, 30, 40]
    data.currentSet = 1
    data.inMatchNavButtons = {
        "Match Stats": [data.width//4 + 30, data.height - 100, data.buttonWidth//3, data.buttonHeight],
        "End Game": [3*data.width//4 - 30, data.height - 100, data.buttonWidth//3, data.buttonHeight]
    }
    data.inMatchButtons = createInMatchButtons(data)
    data.tiebreaker = False
    data.matchOverButtons = {"Home": [data.width // 2, data.height // 2 + 75, 125, 25],
                        "Match Summary": [data.width // 2 - 65, data.height // 2 + 135, 60, 25],
                        "Log Out": [data.width // 2 + 65, data.height // 2 + 135, 60, 25]}
    data.summaryStatsButtons = {
        "Improve Game": [data.width//4 + 30, data.height//4 + 15, data.buttonWidth//3, data.buttonHeight],
        "Play Match": [3*data.width//4 - 30, data.height//4 + 15, data.buttonWidth//3, data.buttonHeight]
    }
    data.summaryStatsLabels = ["1st Serve In", "2nd Serve In", "1st Serve Points Won",
                               "2nd Serve Points Won", "1st Serve Returns In", "2nd Serve Returns In",
                               "1st Serve Return Won", "2nd Serve Return Won"]

    data.matchHistoryButtons = {
        "1st Serve In": [data.width // 8, data.height//4, data.width // 8, 25, True],
        "2nd Serve In": [3 * data.width // 8, data.height//4, data.width // 8, 25, False],
        "1st Serve Points Won": [5 * data.width // 8, data.height//4, data.width // 8, 25, False],
        "2nd Serve Points Won": [7 * data.width // 8, data.height//4, data.width // 8, 25, False],
        "1st Serve Returns In": [data.width // 8, data.height // 4 + 50, data.width // 8, 25, False],
        "2nd Serve Returns In": [3 * data.width // 8, data.height // 4 + 50, data.width // 8, 25, False],
        "1st Serve Return Won": [5 * data.width // 8, data.height // 4 + 50, data.width // 8, 25, False],
        "2nd Serve Return Won": [7 * data.width // 8, data.height // 4 + 50, data.width // 8, 25, False],
    }
    data.simulationButtons = {
        "Improve Game": [data.width//4 + 30, data.height//4 + 15, data.buttonWidth//3, data.buttonHeight],
        "Play Match": [3*data.width//4 - 30, data.height//4 + 15, data.buttonWidth//3, data.buttonHeight]

    }
    data.improveButtons = {
        "Simulation": [data.width//4 + 30, data.height//4 + 15, data.buttonWidth//3, data.buttonHeight],
        "Play Match": [3*data.width//4 - 30, data.height//4 + 15, data.buttonWidth//3, data.buttonHeight]

    }
    data.changeover = False
    data.winning = None
    data.currentGraph = data.summaryStatsLabels[0]
####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "login"): loginMousePressed(event, data)
    elif (data.mode == "home"):   homeMousePressed(event, data)
    elif (data.mode == "help"): helpMousePressed(event, data)
    elif (data.mode == "startMatch"):   startMatchMousePressed(event, data)
    elif (data.mode == "inMatch"):  inMatchMousePressed(event, data)
    elif (data.mode == "summaryStats"): summaryStatsMousePressed(event, data)
    elif (data.mode == "simulation"):   simulationMousePressed(event, data)
    elif (data.mode == "improve"):  improveMousePressed(event, data)
    elif (data.mode == "matchOver"):  matchOverMousePressed(event, data)
    elif (data.mode == "matchHistory"): matchHistoryMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "login"): loginKeyPressed(event, data)
    elif (data.mode == "home"):   homeKeyPressed (event, data)
    elif (data.mode == "help"): helpKeyPressed(event, data)
    elif (data.mode == "startMatch"):   startMatchKeyPressed(event, data)
    elif (data.mode == "inMatch"):  inMatchKeyPressed(event, data)
    elif (data.mode == "summaryStats"): summaryStatsKeyPressed(event, data)
    elif (data.mode == "simulation"):   simulationKeyPressed(event, data)
    elif (data.mode == "improve"):  improveKeyPressed(event, data)
    elif (data.mode == "matchOver"):  matchOverKeyPressed(event, data)
    elif (data.mode == "matchHistory"): matchHistoryKeyPressed(event, data)

def redrawAll(canvas, data):
    if (data.mode == "login"): loginRedrawAll(canvas, data)
    elif (data.mode == "home"):   homeRedrawAll(canvas, data)
    elif (data.mode == "help"): helpRedrawAll(canvas, data)
    elif (data.mode == "startMatch"):   startMatchRedrawAll(canvas, data)
    elif (data.mode == "inMatch"):  inMatchRedrawAll(canvas, data)
    elif (data.mode == "summaryStats"): summaryStatsRedrawAll(canvas, data)
    elif (data.mode == "simulation"):   simulationRedrawAll(canvas, data)
    elif (data.mode == "improve"):  improveRedrawAll(canvas, data)
    elif (data.mode == "matchOver"): matchOverRedrawAll(canvas, data)
    elif (data.mode == "matchHistory"): matchHistoryRedrawAll(canvas, data)

####################################
# run entire gui
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

# run(500, 800)


