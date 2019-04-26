'''
Citation: Tennis simulation code taken from https://github.com/shawnberry/Tennis. Modified significantly to account for
different game scores, set scores, tie break scores. Generates Player 1's and Player 2's simulation stats (compilation of winning stats in
the simulation). Previous simulation code only took into consideration a player's probability of winning point on their serve. --> Modified code
considers each player's 1st Serve %, 2nd Serve %, 1st Serve Points Won %, 2nd Serve Points Won %, 1st Serve Return %, 2nd Serve Return % to run an
accurate simulation of each point. Finds the key stats that are necessary for each player to win the match by running 10,000 simulations
of the match (based on current inputs shown above), and averages the key stats for each simulation that the player won.

TP1: When you run the code, it will print out all 10,000 simulations that run as well as the current real match stats for P1 and P2,
and the key stats for P1 to win, and P2 to lose based on the simulation. You can modify this by going to runSimulationLotsOfTimes - line 400.
You can also test out different starting input values by going to lines 254-283. Running 10,000 simulations takes approx. 10-15 seconds.
'''

from random import random
import math
from Class.playerClass import Player
from GUI import inMatchScreen
'Try to Create a Simulation Class'
def runMatchSimulation(data):
    # def getInputs():
    #     p1, a = input(
    #         "Input name of Player 1, probability (0, 1) that Player 1 wins a serve: ").split(
    #         ",")
    #     p2, b = input(
    #         "Input name of Player 2, probability (0, 1) that Player 2 wins a serve: ").split(
    #         ",")
    #     p1, p2 = p1.strip(), p2.strip()  # Remove any surrounding spaces
    #     a, b = float(a), float(b)  # Str --> Float
    #     print()
    #     return p1, p2, a, b


    # Simulate A Set

    def simulateSet(gamesMatch, S, pointsMatch1, pointsMatch2, gamesSet1, gamesSet2, p1Stats, p2Stats, p1SimulationStats, p2SimulationStats):
        S += 1  # Set number S
        # gamesSet1, gamesSet2 = 0, 0  # At start of new Set, reset Games Won in this Set by Player1, Player2 to 0, 0

        while (max(gamesSet1, gamesSet2) < 6 or abs(gamesSet1 - gamesSet2) < 2) and gamesSet1 + gamesSet2 < 12:
            # Conditions to play another Game in this Set
            pointsGame1, pointsGame2 = 0, 0  # At start of new Game, reset Points Won in this Game by Player1, Player2 to 0, 0

            while gamesMatch % 2 == 0:  # Player1 serves if Games played in Match is Even
                pointsGame1, pointsGame2, p1SimulationStats, p2SimulationStats = \
                    simulatePoint(p1Stats, p2Stats, pointsGame1, pointsGame2, p1SimulationStats, p2SimulationStats)

                if max(pointsGame1, pointsGame2) >= 4 and abs(pointsGame1 - pointsGame2) > 1:  # Conditions to stop Game (race to 4, win by 2)
                    print("\t", p1 + ":", str(pointsGame1) + ",", p2 + ":", pointsGame2, end="")
                    # Print score of Game to screen (recap of documented letters at L)
                    if pointsGame1 > pointsGame2:  # Condition that Player1 won this completed Game
                        gamesSet1 += 1  # Increment Games won in this Set by Player1
                        print()  # Player serving held serve/No break of serve to highlight, Next line
                    else:  # Condition that Player2 won this completed Game
                        gamesSet2 += 1  # Increment Games won in this Set by Player2
                        print(" -- " + p2, "broke")  # Highlight that Player2 broke (won a non-service Game), Next line
                    gamesMatch += 1  # Increment Games completed in the Match
                    break
            pointsMatch1 += pointsGame1
            pointsMatch2 += pointsGame2

            pointsGame1, pointsGame2 = 0, 0  # At start of new Game, reset Points Won in this Game by Player1, Player2 to 0, 0
            while gamesMatch % 2 == 1 and (max(gamesSet1, gamesSet2) < 6 or abs(gamesSet1 - gamesSet2) < 2) \
                    and gamesSet1 + gamesSet2 < 12:
                # Conditions to play another Game in this Set and Player2 serves if Games played in Match is Odd
                pointsGame2, pointsGame1, p2SimulationStats, p1SimulationStats = \
                    simulatePoint(p2Stats, p1Stats, pointsGame2, pointsGame1, p2SimulationStats, p1SimulationStats)

                if max(pointsGame1, pointsGame2) >= 4 and abs(
                        pointsGame1 - pointsGame2) > 1:  # Conditions to stop Game (race to 4, win by 2)
                    print("\t", p1 + ":", str(pointsGame1) + ",", p2 + ":",
                          pointsGame2,
                          end="")  # Print score of Game to screen (recap of documented letters at L)
                    if pointsGame1 > pointsGame2:  # Condition that Player1 won this completed Game
                        gamesSet1 += 1  # Increment Games won in this Set by Player1
                        print(" -- " + p1,
                              "broke")  # Highlight that Player1 broke (won a non-service Game), Next line
                    else:  # Condition that Player2 won this completed game
                        gamesSet2 += 1  # Increment Games won in this Set by Player2
                        print()  # Player serving held serve/No break of serve to highlight, Next line
                    gamesMatch += 1  # Increment Games completed in the Match
                    break
            pointsMatch1 += pointsGame1
            pointsMatch2 += pointsGame2

        if gamesSet1 == 6 and gamesSet2 == 6:  # Conditions to start Tiebreaker
            print("Set", S, "is 6-6 and going to a Tiebreaker.")

        return gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2, p1SimulationStats, p2SimulationStats


    # Simulate Tiebreaker
    def simulateTiebreaker(gamesMatch, pointsMatch1, pointsMatch2, p1Stats, p2Stats, p1SimulationStats, p2SimulationStats):
        pointsTie1, pointsTie2 = 0, 0  # At start of Tiebreaker, reset points Won by Player1, Player2 to 0, 0
        while max(pointsTie1, pointsTie2) < 7 or abs(
                pointsTie1 - pointsTie2) < 2:  # Conditions to continue Tiebreaker (race to 7, win by 2)

            if gamesMatch % 2 == 0:  # Condition for Player1 to serve first in Tiebreaker

                while (pointsTie1 + pointsTie2) % 4 == 0 or (
                        pointsTie1 + pointsTie2) % 4 == 3:  # Conditions for Player 1 to serve (points 4N and 4N+3)
                    pointsTie1, pointsTie2, p1SimulationStats, p2SimulationStats = \
                        simulatePoint(p1Stats, p2Stats, pointsTie1, pointsTie2, p1SimulationStats, p2SimulationStats)

                    if max(pointsTie1, pointsTie2) >= 7 and abs(
                            pointsTie1 - pointsTie2) > 1:  # Conditions to stop Tiebreaker (race to 7, win by 2)
                        print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":",
                              pointsTie2)  # Print score of Tiebreaker to screen (recap of documented letters at L)
                        gamesMatch += 1
                        break
                pointsMatch1 += pointsTie1
                pointsMatch2 += pointsTie2

                while (max(pointsTie1, pointsTie2) < 7 or abs(
                        pointsTie1 - pointsTie2) < 2) and (
                        (pointsTie1 + pointsTie2) % 4 == 1 or (
                        pointsTie1 + pointsTie2) % 4 == 2):
                    # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N+1 and 4N+2)

                    pointsTie2, pointsTie1, p2SimulationStats, p1SimulationStats = \
                        simulatePoint(p2Stats, p1Stats, pointsTie2, pointsTie1, p2SimulationStats, p1SimulationStats)

                    if max(pointsTie1, pointsTie2) >= 7 and abs(
                            pointsTie1 - pointsTie2) > 1:  # Conditions to stop Tiebreaker (race to 7, win by 2)
                        print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":",
                              pointsTie2)  # Print score of Tiebreaker to screen (recap of documented letters at L)
                        break
                pointsMatch1 += pointsTie1
                pointsMatch2 += pointsTie2

            if gamesMatch % 2 == 1:  # Condition for Player2 to serve first in Tiebreaker
                while (pointsTie1 + pointsTie2) % 4 == 1 or (
                        pointsTie1 + pointsTie2) % 4 == 2:  # Conditions for Player 1 to serve (points 4N+1 and 4N+2)

                    pointsTie1, pointsTie2, p1SimulationStats, p2SimulationStats = \
                        simulatePoint(p1Stats, p2Stats, pointsTie1, pointsTie2, p1SimulationStats, p2SimulationStats)

                    if max(pointsTie1, pointsTie2) >= 7 and abs(
                            pointsTie1 - pointsTie2) > 1:  # Conditions to stop Tiebreaker (race to 7, win by 2)
                        print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":",
                              pointsTie2)  # Print score of Tiebreaker to screen (recap of documented letters at L)
                        gamesMatch += 1
                        break
                pointsMatch1 += pointsTie1
                pointsMatch2 += pointsTie2

                while (max(pointsTie1, pointsTie2) < 7 or abs(
                        pointsTie1 - pointsTie2) < 2) and (
                        (pointsTie1 + pointsTie2) % 4 == 0 or (
                        pointsTie1 + pointsTie2) % 4 == 3):
                    # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N and 4N+3)
                    pointsTie2, pointsTie1, p2SimulationStats, p1SimulationStats = \
                        simulatePoint(p2Stats, p1Stats, pointsTie2, pointsTie1, p2SimulationStats, p1SimulationStats)

                    if max(pointsTie1, pointsTie2) >= 7 and abs(
                            pointsTie1 - pointsTie2) > 1:  # Conditions to stop Tiebreaker (race to 7, win by 2)
                        print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":",
                              pointsTie2)  # Print score of Tiebreaker to screen (recap of documented letters at L)
                        break
                pointsMatch1 += pointsTie1
                pointsMatch2 += pointsTie2

        gamesMatch += 1
        return pointsTie1, pointsTie2, gamesMatch, pointsMatch1, pointsMatch2, p1SimulationStats, p2SimulationStats


    ##### Print Set Summary

    def printSetMatchSummary(p1, p2, gamesSet1, gamesSet2, S, pointsTie1,
                             pointsTie2, setsMatch1, setsMatch2):

        if gamesSet1 > gamesSet2:
            setsMatch1 += 1
            print(p1.upper(), "wins Set", str(S) + ":", gamesSet1, "games to",
                  str(gamesSet2) + ".")

        elif gamesSet2 > gamesSet1:
            setsMatch2 += 1
            print(p2.upper(), "wins Set", str(S) + ":", gamesSet2, "games to",
                  str(gamesSet1) + ".")

        elif gamesSet1 == gamesSet2:
            if pointsTie1 > pointsTie2:
                setsMatch1 += 1
                print(p1.upper(), "wins Set",
                      str(S) + ": 7 games to 6 (" + str(pointsTie1) + "-" + str(
                          pointsTie2) + ").")
            else:
                setsMatch2 += 1
                print(p2.upper(), "wins Set",
                      str(S) + ": 7 games to 6 (" + str(pointsTie2) + "-" + str(
                          pointsTie1) + ").")

        print("After", S, "Sets:", p1, str(setsMatch1) + ",", p2,
              str(setsMatch2) + ".\n")

        return setsMatch1, setsMatch2

    ##### Points Match Summary

    def pointsMatchSummary(p1, p2, setsMatch1, setsMatch2, pointsMatch1,
                           pointsMatch2):
        if setsMatch1 == 3:
            print(p1.upper(), "(" + str(a) + ")", "beat", p2,
                  "(" + str(b) + ") by", setsMatch1, "Sets to",
                  str(setsMatch2) + ".")
        else:
            print(p2.upper(), "(" + str(b) + ")", "beat", p1,
                  "(" + str(a) + ") by", setsMatch2, "Sets to",
                  str(setsMatch1) + ".")
        print("Of", pointsMatch1 + pointsMatch2, "points played,", p1, "won",
              pointsMatch1, "(" + str(
                round(pointsMatch1 / (pointsMatch1 + pointsMatch2),
                      3)) + ") and", p2, "won", pointsMatch2, "(" + str(
                round(pointsMatch2 / (pointsMatch1 + pointsMatch2), 3)) + ").")

    # Starting variables
    totalNumSets = data.match.totalNumSets
    S = data.currentSet
    startS = data.currentSet
    gamesMatch = data.match.totalGamesMatch
    pointsMatch1, pointsMatch2 = data.p1.pointsMatch, data.p2.pointsMatch
    setsMatch1, setsMatch2 = data.p1.setsMatch, data.p2.setsMatch
    gamesSet1, gamesSet2 = data.p1.gamesSet, data.p2.gamesSet
    pointsTie1, pointsTie2 = data.p1.pointsTie, data.p2.pointsTie
    # p1 is player who served first
    p1, p2, a, b = data.p1.name, data.p2.name, "Player 1", "Player 2"

    # p1 Serve Stats
    p1FirstServeIn = data.p1.averageStats[0]
    p1SecondServeIn = data.p1.averageStats[1]
    # p1 Serve Win
    p1FirstServeWin = data.p1.averageStats[2]
    p1SecondServeWin = data.p1.averageStats[3]
    # p1 Return Stats
    p1FirstServeReturnIn = data.p1.averageStats[4]
    p1SecondServeReturnIn = data.p1.averageStats[5]

    # p2 Serve Stats
    p2FirstServeIn = data.p2.averageStats[0]
    p2SecondServeIn = data.p2.averageStats[1]
    # p2 Serve Win
    p2FirstServeWin = data.p2.averageStats[2]
    p2SecondServeWin = data.p2.averageStats[3]
    # p2 Return Stats
    p2FirstServeReturnIn = data.p2.averageStats[4]
    p2SecondServeReturnIn = data.p2.averageStats[5]

    # match stats
    p1Stats = [p1FirstServeIn, p1SecondServeIn, p1FirstServeWin,
               p1SecondServeWin, p1FirstServeReturnIn, p1SecondServeReturnIn]
    p2Stats = [p2FirstServeIn, p2SecondServeIn, p2FirstServeWin,
               p2SecondServeWin, p2FirstServeReturnIn, p2SecondServeReturnIn]

    # SimulationStats = [[firstServesMade], [secondServesMade],
    # [firstServePointsWon], [secondServePointsWon], [firstReturnsMade], [secondReturnsMade]]

    p1SimulationStats = [[], [], [], [], [], [], [], []]
    p2SimulationStats = [[], [], [], [], [], [], [], []]

    def simulatePoint(server, returner, serversPoints, returnersPoints, serverSS, returnerSS):
        firstServeIn, secondServeIn, firstServeWin, secondServeWin = \
            server[0], server[1], server[2], server[3] # takes the stats from the given tuple
        firstServeReturnIn, secondServeReturnIn = returner[4], returner[5]

        # simulation stats
        firstServesMade, secondServesMade, firstServePointsWon, secondServePointsWon = \
            serverSS[0], serverSS[1], serverSS[2], serverSS[3]
        firstServeReturnsMade, secondServeReturnsMade, firstServeReturnWon, secondServeReturnWon = \
            returnerSS[4], returnerSS[5], returnerSS[6], returnerSS[7]

        # random generators
        isFirstServeIn = random()
        isFirstReturnIn = random()
        isFirstServeWin = random()
        isSecondServeIn = random()
        isSecondReturnIn = random()
        isSecondServeWin = random()


        if isFirstServeIn < firstServeIn: # is the first serve is in
            firstServesMade.append(1)
            if isFirstReturnIn < firstServeReturnIn: # is the return in
                firstServeReturnsMade.append(1)

                if isFirstServeWin < firstServeWin: # find who won the point
                    firstServePointsWon.append(1)
                    firstServeReturnWon.append(0) #--> keep track of return won on 1st 2nd Serve %
                    serversPoints += 1
                else:
                    firstServePointsWon.append(0)
                    firstServeReturnWon.append(1)
                    returnersPoints += 1
            else:
                firstServeReturnsMade.append(0)
                # firstServePointsWon.append(1)
                serversPoints += 1
            return serversPoints, returnersPoints, serverSS, returnerSS

        elif isSecondServeIn < secondServeIn: # is the second serve in
            firstServesMade.append(0)
            secondServesMade.append(1)
            if isSecondReturnIn < secondServeReturnIn: # is the return in
                secondServeReturnsMade.append(1)
                if isSecondServeWin < secondServeWin:
                    secondServePointsWon.append(1)
                    secondServeReturnWon.append(0)
                    serversPoints += 1
                else:
                    secondServePointsWon.append(0)
                    secondServeReturnWon.append(1)
                    returnersPoints += 1
            else:
                secondServeReturnsMade.append(0)
                # secondServePointsWon.append(1)
                serversPoints += 1
            return serversPoints, returnersPoints, serverSS, returnerSS

        # otherwise it is a double fault
        else:
            firstServesMade.append(0)
            secondServesMade.append(0)
            returnersPoints += 1
            return serversPoints, returnersPoints, serverSS, returnerSS

    while S <= totalNumSets and max(setsMatch1, setsMatch2) < math.ceil(totalNumSets/2):
        if S is not startS:
            gamesSet1, gamesSet2 = 0, 0

        gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2, p1SimulationStats, p2SimulationStats = \
            simulateSet(gamesMatch, S, pointsMatch1, pointsMatch2, gamesSet1, gamesSet2, p1Stats, p2Stats, p1SimulationStats, p2SimulationStats)

        print()

        if gamesSet1 == 6 and gamesSet2 == 6:
            pointsTie1, pointsTie2, gamesMatch, pointsMatch1, pointsMatch2, p1SimulationStats, p2SimulationStats = \
                simulateTiebreaker(gamesMatch, pointsMatch1, pointsMatch2, p1Stats, p2Stats, p1SimulationStats, p2SimulationStats)

        setsMatch1, setsMatch2 = printSetMatchSummary(p1, p2, gamesSet1,
                                                      gamesSet2, S, pointsTie1,
                                                      pointsTie2, setsMatch1,
                                                      setsMatch2)
    pointsMatchSummary(p1, p2, setsMatch1, setsMatch2, pointsMatch1, pointsMatch2)
    return setsMatch1, setsMatch2, p1SimulationStats, p2SimulationStats, p1Stats, p2Stats

def averageSimMatchStats(simStats, totalSim):
    for i, stats in enumerate(simStats):
        if len(stats) > 0:
            p = sum(stats) / len(stats)
            totalSim[i].append(p)
    return totalSim

def findKeysToMatch(totalSimStats):
    for i, stats in enumerate(totalSimStats):
        if len(stats) > 0:
            p = sum(stats) / len(stats)
            totalSimStats[i] = p
        else:
            totalSimStats[i] = 0.5
    return totalSimStats

def printMatchStats(player, totalSimStats):
    firstServesMade = round((totalSimStats[0] * 100), 2)
    print(player + " --> Make " + str(firstServesMade) + "% first serves")

    secondServesMade = round((totalSimStats[1] * 100), 2)
    print(player + " --> Make " + str(secondServesMade) + "% second serves")

    firstServePointsWon = round((totalSimStats[2] * 100), 2)
    print(player + " --> Win " + str(firstServePointsWon) + "% first serve points")

    secondServePointsWon = round((totalSimStats[3] * 100), 2)
    print(player + " --> Win " + str(secondServePointsWon) + "% second serve points")

    firstReturnsMade = round((totalSimStats[4] * 100), 2)
    print(player + " --> Make " + str(firstReturnsMade) + "% first serve returns")

    secondReturnsMade = round((totalSimStats[5] * 100), 2)
    print(player + " --> Make " + str(secondReturnsMade) + "% second serve returns")

def runSimulationLotsOfTimes(data):
    p1TotalSimStats = [[], [], [], [], [], [], [], []]
    p2TotalSimStats = [[], [], [], [], [], [], [], []]
    totalNumSets = data.match.totalNumSets
    runNum, totalRunNum = 0, 10000
    numMatchesWon1, numMatchesWon2 = 0, 0
    while runNum < totalRunNum:
        print("Run Num: ", runNum)
        setsMatch1, setsMatch2, p1SimulationStats, p2SimulationStats, p1Stats, p2Stats = runMatchSimulation(data)
        if setsMatch1 == math.ceil(totalNumSets/2):
            numMatchesWon1 += 1
            p1TotalSimStats = averageSimMatchStats(p1SimulationStats, p1TotalSimStats)

        if setsMatch2 == math.ceil(totalNumSets/2): # if player 2 wins
            numMatchesWon2 += 1
            p2TotalSimStats = averageSimMatchStats(p2SimulationStats, p2TotalSimStats)

        runNum += 1

    percMatchesWon1 = (numMatchesWon1/totalRunNum)*100
    percMatchesWon2 = (numMatchesWon2/totalRunNum)*100
    print()
    print("P1 won: " + str(round(percMatchesWon1, 2)) + "% of the time")
    print("P2 won: " + str(round(percMatchesWon2, 2)) + "% of the time")

    p1TotalSimStats = findKeysToMatch(p1TotalSimStats)
    p2TotalSimStats = findKeysToMatch(p2TotalSimStats)

    print()
    print("Player 1 Current Match Stats")
    printMatchStats("Player 1", p1Stats)
    print()
    print("Player 2 Current Match Stats")
    printMatchStats("Player 2", p2Stats)

    return p1TotalSimStats, p2TotalSimStats, percMatchesWon1, percMatchesWon2

