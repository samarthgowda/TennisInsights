import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np
import json

# file for creating and downloading the match history graphs as images

def readFile(path):
    with open(path) as f:
        d = json.load(f)
        return d

def writeFile(path, contents):
    with open(path, "w") as f:
        jsonData = json.dump(contents, f)
        return jsonData

def drawGraphs(data):
    if plt:
        plt.clf()
    d = readFile("users/"+data.email+".json")
    label = data.currentGraph
    y = d[label]
    x = d["date"]
    plt.plot(x, y)
    plt.axis(ymin = 0, ymax = 1)
    plt.xlabel("Match Dates")
    plt.ylabel(label + "%")
    plt.savefig('graphs/'+label+".png", dpi = 70)


