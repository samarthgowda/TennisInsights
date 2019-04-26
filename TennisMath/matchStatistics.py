# general functions to calculate the match stats, score, serving, etc.

import math

def findAveragePlayerStats(playerStats):
    result = []
    for stats in (playerStats):
        if len(stats) > 0:
            p = sum(stats) / len(stats)
            result.append(p)
        else:
            result.append(0)
    return result

def findGameDisplayScore(data, playerGamePoints, otherPlayerGamePoints):
    if playerGamePoints <= 3:
        displayScore = data.tennisGameScoring[playerGamePoints]
        return displayScore
    else:
        if playerGamePoints <= otherPlayerGamePoints:
            return 40
        else:
            return "AD"


def updateSet(data):
    # Conditions to play another Game in this Set
    if (max(data.p1.gamesSet, data.p2.gamesSet) < 6 or abs(data.p1.gamesSet - data.p2.gamesSet) < 2) \
            and data.p1.gamesSet + data.p2.gamesSet < 12:
        # At start of new Game, reset Points Won in this Game by Player1, Player2 to 0, 0
        if data.match.totalGamesMatch % 2 == 0:  # Player1 serves if Games played in Match is Even
            if data.p1.name == "You":
                data.serving = True
            else:
                data.serving = False
        # Conditions to play another Game in this Set and Player2 serves if Games played in Match is Odd
        if data.match.totalGamesMatch % 2 == 1:
            if data.p2.name == "You":
                data.serving = True
            else:
                data.serving = False
            ###### play the point here #####
        # Conditions to stop Game (race to 4, win by 2)
        if max(data.p1.pointsGame, data.p2.pointsGame) >= 4 and abs(data.p1.pointsGame - data.p2.pointsGame) > 1:
            if data.p1.pointsGame > data.p2.pointsGame:  # Condition that Player1 won this completed Game
                data.p1.gamesSet += 1  # Increment Games won in this Set by Player1
            else:  # Condition that Player2 won this completed Game
                data.p2.gamesSet += 1  # Increment Games won in this Set by Player2
            data.match.totalGamesMatch += 1  # Increment Games completed in the Match
            data.p1.pointsGame, data.p2.pointsGame = 0, 0  # At start of new Game, reset Points Won in this Game by Player1, Player2 to 0, 0
            data.serving = not data.serving

    data.p1.setScores[data.currentSet-1] = data.p1.gamesSet
    data.p2.setScores[data.currentSet-1] = data.p2.gamesSet

    if max(data.p1.gamesSet, data.p2.gamesSet) == 6 and abs(data.p1.gamesSet - data.p2.gamesSet) >=2 \
            or abs(data.p1.gamesSet - data.p2.gamesSet) == 2 and (data.p1.gamesSet + data.p2.gamesSet) == 12:
        if data.p1.gamesSet > data.p2.gamesSet:
            data.p1.setsMatch += 1
        else:
            data.p2.setsMatch += 1
        data.currentSet += 1  # Set number S
        data.p1.gamesSet, data.p2.gamesSet = 0, 0

    if data.p1.gamesSet == 6 and data.p2.gamesSet == 6:  # Conditions to start Tiebreaker
        data.tiebreaker = True
        updateTiebreaker(data)

    if max(data.p1.setsMatch, data.p2.setsMatch) == math.ceil(data.match.totalNumSets/2):
        # if data.p1.setsMatch < data.p2.setsMatch:
        #     data.won = False
        # else:
        #     data.won = True
        # data.matchOver = True
        data.mode = "matchOver"

    return


def updateTiebreaker(data):
    # At start of Tiebreaker, reset points Won by Player1, Player2 to 0, 0
    if max(data.p1.pointsTie, data.p2.pointsTie) < 7 or abs(data.p1.pointsTie - data.p2.pointsTie) < 2:
        # Conditions to continue Tiebreaker (race to 7, win by 2)

        if data.match.totalGamesMatch % 2 == 0:  # Condition for Player1 to serve first in Tiebreaker
            if data.p1.name == "You":
                data.serving = True
            else:
                data.serving = False

            # Conditions for Player 1 to serve (points 4N and 4N+3)
            if (data.p1.pointsTie + data.p2.pointsTie) % 4 == 0 or (data.p1.pointsTie + data.p2.pointsTie) % 4 == 3:
                if data.p1.name == "You":
                    data.serving = True
                else:
                    data.serving = False
                ###### play the point here #####


            if (max(data.p1.pointsTie, data.p2.pointsTie) < 7 or abs(
                    data.p1.pointsTie - data.p2.pointsTie) < 2) and (
                    (data.p1.pointsTie + data.p2.pointsTie) % 4 == 1 or (
                    data.p1.pointsTie + data.p2.pointsTie) % 4 == 2):
                # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N+1 and 4N+2)
                if data.p2.name == "You":
                    data.serving = True
                else:
                    data.serving = False
                ### play point here ###

        if data.match.totalGamesMatch % 2 == 1:  # Condition for Player2 to serve first in Tiebreaker
            if data.p2.name == "You":
                data.serving = True
            else:
                data.serving = False

            if (data.p1.pointsTie + data.p2.pointsTie) % 4 == 1 or (
                    data.p1.pointsTie + data.p2.pointsTie) % 4 == 2:
                # Conditions for Player 1 to serve (points 4N+1 and 4N+2)
                if data.p1.name == "You":
                    data.serving = True
                else:
                    data.serving = False
                ###### play the point here #####

            if (max(data.p1.pointsTie, data.p2.pointsTie) < 7 or abs(data.p1.pointsTie - data.p2.pointsTie) < 2) \
                    and ((data.p1.pointsTie + data.p2.pointsTie) % 4 == 0 or (data.p1.pointsTie + data.p2.pointsTie) % 4 == 3):
                # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N and 4N+3)
                if data.p2.name == "You":
                    data.serving = True
                else:
                    data.serving = False
                ###### play the point here #####

    if max(data.p1.pointsTie, data.p2.pointsTie) >= 7 and abs(data.p1.pointsTie - data.p2.pointsTie) > 1:
        data.match.totalGamesMatch += 1

        if data.p1.pointsTie > data.p2.pointsTie:
            data.p1.setsMatch += 1
            data.p1.gamesSet += 1
        else:
            data.p2.setsMatch += 1
            data.p2.gamesSet += 1

        data.p1.setScores[data.currentSet - 1] = data.p1.gamesSet
        data.p2.setScores[data.currentSet - 1] = data.p2.gamesSet

        data.match.totalGamesMatch += 1
        data.p1.pointsGame, data.p2.pointsGame = 0, 0
        data.p1.pointsTie, data.p2.pointsTie = 0, 0
        data.p1.gamesSet, data.p2.gamesSet = 0, 0
        data.currentSet += 1  # Set number S
        data.tiebreaker = False
        data.serving = not data.serving


    return

