class Player(object):

    def __init__(self, name):
        # self.player = player # p1 or p2
        self.name = name
        self.stats = [[], [], [], [], [], [], [], []]
        self.averageStats = [[], [], [], [], [], [], [], []]
        # stats = [[firstServesMade] - 0, [secondServesMade] - 1, [firstServePointsWon] - 2
        # , [secondServePointsWon] - 3, [firstReturnsMade] - 4, [secondReturnsMade] - 5]
        self.pointsMatch = 0 # total points won in the match
        self.setsMatch = 0 # num of sets won in the match
        self.gamesSet = 0 # games won in the set
        self.pointsGame = 0 # points won in the game
        self.pointsTie = 0 # points won in the tiebreak
        self.setScores = [0,0,0,0,0] # list with the set score --> for drawing
        self.improve = []

    def firstServeMade(self, make): #self.Stats[0]
        firstServeList = self.stats[0]
        if make:
            firstServeList.append(1)
        else:
            firstServeList.append(0)

    def secondServeMade(self, make): #self.Stats[1]
        secondServeList = self.stats[1]
        if make:
            secondServeList.append(1)
        else:
            secondServeList.append(0)

    def firstServePointWon(self, won): #self.Stats[2]
        firstServePointList = self.stats[2]
        if won:
            firstServePointList.append(1)
        else:
            firstServePointList.append(0)

    def secondServePointWon(self, won): #self.Stats[3]
        secondServePointList = self.stats[3]
        if won:
            secondServePointList.append(1)
        else:
            secondServePointList.append(0)

    def firstReturnMade(self, make): #self.Stats[4]
        firstReturnList = self.stats[4]
        if make:
            firstReturnList.append(1)
        else:
            firstReturnList.append(0)

    def secondReturnMade(self, make): #self.Stats[5]
        secondReturnList = self.stats[5]
        if make:
            secondReturnList.append(1)
        else:
            secondReturnList.append(0)

    def firstServeReturnWon(self, won):
        firstReturnWonList = self.stats[6]
        if won:
            firstReturnWonList.append(1)
        else:
            firstReturnWonList.append(0)

    def secondServeReturnWon(self, won):
        secondReturnWonList = self.stats[7]
        if won:
            secondReturnWonList.append(1)
        else:
            secondReturnWonList.append(0)

    def findAveragePlayerStats(self): # average all of the 1 & 0 values to find the percentages
        averageStats = []
        for i, stat in enumerate(self.stats):
            if len(stat) > 0:
                p = sum(stat) / len(stat)
                averageStats.insert(i, p)
            else:
                averageStats.insert(i, 0.5)
        self.averageStats = averageStats

def testPlayerStats():
    p1 = Player("Sam")
    import random
    n = 100
    while n > 0:
        choiceList = [p1.firstServeMade, p1.secondServeMade, p1.firstServePointWon,
                      p1.secondServePointWon, p1.firstReturnMade, p1.secondReturnMade]
        made = [True, False]
        f = random.choice(choiceList)
        value = random.choice(made)
        f(value)
        n -= 1
    p1Stats = p1.findAveragePlayerStats()
    return p1Stats