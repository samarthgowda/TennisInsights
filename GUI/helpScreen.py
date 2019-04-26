from GUI.startMatchScreen import *
def helpMousePressed(event, data):
    if navClicked(event, data): return

def helpKeyPressed(event, data):
    if event.keysym == "h":
        data.mode = "home"

def helpRedrawAll(canvas, data):
    canvas.create_image(0, 0, anchor = "nw", image = data.helpScreenBackground)
    drawNavigation(canvas, data)
