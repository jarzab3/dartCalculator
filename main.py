import time
from prettytable import PrettyTable
from scoringTable import *

def selectGame():
    while True:
        try:
            query = "\nGame 301 type: 1\nGame 501 type: 2\n"
            userInput = int(input(query))
            if userInput != 1 and userInput != 2:
                print("Please input valid choice")
                continue

        except ValueError:
            print("Incorrect input, please try again")
            continue

        else:
            print ("\n")
            if userInput == 1:
                totalScores = 301
            if userInput == 2:
                totalScores = 501
            return totalScores


def takeUsersNames(numberOfPlayer, noPlayer):
    while True:
        try:
            query = str(noPlayer + 1) + " player name? "
            userInput = str(input(query))
            if userInput.isdigit():
                print("Please input a string")
                continue
            elif len(userInput) == 0:
                print("Incorrect input, please try again")
                continue
        except ValueError:
            if userInput.isdigit():
                print("Please input a string")
            else:
                print("Incorrect input, please try again")

        else:
            userName = userInput.upper()
            userName = userName.replace(" ", "")
            return userName


def takeUsersInput(playersName):
    pointsInput = 0
    while True:
        try:
            playerFormatted = "Input points for player " + playersName + ": "
            pointsInput = int(input(playerFormatted))
            if pointsInput > 60:
                print("Incorrect input, value cannot be above '60'\n")
                continue
        except ValueError:
            if not isinstance(pointsInput, int):
                print("Please input a integer")
            
            else:
                print("Incorrect input, please try again")

            continue

        else:
            return pointsInput


def updateStats(player, dataForStats):

    currentStatsForPlayer = player[2]
    currentPlayerPoints = player[1]

    currentPlayerTotalPoints = dataForStats[3]

    newAttempts = currentStatsForPlayer["throws"] + dataForStats[1]

    newAverage = currentPlayerTotalPoints / newAttempts

    newtimePlayed = int(currentStatsForPlayer["timePlayed"]) + int(dataForStats[2])

    updatedStats = {"average": newAverage, "throws": newAttempts, "timePlayed": newtimePlayed}

    return updatedStats


def calcPoints(currentPlayer, points):

    currentPlayerPoints = currentPlayer[1]
    currentPlayerName = currentPlayer[0]
    currentPlayerTotalPoints = currentPlayer[3]


    # Temporary points var
    tempPoints = 0

    # Points to return to and total to add to a user
    pointsToAddToPlayer = 0

    maxAttempts = 3
    attempts = 1
    timePlayed = 0

    startTime = time.time()

    while (attempts <= maxAttempts):
        if currentPlayerPoints - tempPoints < 170:
            found = False
            # Display points for a user if the score is below 170 points, then use knows how should shoot
            for a in finishes:
                if int(a[0]) == (currentPlayerPoints - tempPoints):
                    print ("                                   Scores: {}  --- Try: {}".format((currentPlayerPoints - tempPoints), a[1]))
                    found = True

            if not found:
                print ("                                   Scores: {}".format(currentPlayerPoints - tempPoints))


        userInput = takeUsersInput(currentPlayerName)

        if userInput == 999:
            print ("You need to throw better")
            timePlayed = time.time() - startTime
            dataForStats = [tempPoints, attempts, timePlayed, currentPlayerTotalPoints + tempPoints]
            updatedStats = updateStats(currentPlayer, dataForStats)
            return [True, updatedStats, currentPlayerTotalPoints + tempPoints]

        tempPoints = tempPoints + userInput

        check = (currentPlayerPoints - tempPoints)

        if check < 0 or check == 1:
            print ("                                   Your points are not counted in!")
            timePlayed = time.time() - startTime
            dataForStats = [tempPoints, attempts , timePlayed, currentPlayerTotalPoints + tempPoints]
            updatedStats = updateStats(currentPlayer, dataForStats)
            return [True, updatedStats, currentPlayerTotalPoints + tempPoints]

        elif check == 0:
            timePlayed = time.time() - startTime
            dataForStats = [tempPoints, attempts, timePlayed, currentPlayerTotalPoints + tempPoints]
            updatedStats = updateStats(currentPlayer, dataForStats)
            return [False, updatedStats, currentPlayerTotalPoints + tempPoints]

        elif check == 1:
            print ("                                   Your points are not counted in!")
            timePlayed = time.time() - startTime
            dataForStats = [tempPoints, attempts, timePlayed, currentPlayerTotalPoints + tempPoints]
            updatedStats = updateStats(currentPlayer, dataForStats)
            return [True, updatedStats, currentPlayerTotalPoints + tempPoints]
        else:
            attempts = attempts + 1

    #Otherwise add points to a player
    pointsToAddToPlayer = currentPlayerPoints - tempPoints
    timePlayed = time.time() - startTime
    dataForStats = [tempPoints, attempts - 1, timePlayed, currentPlayerTotalPoints + tempPoints]
    updatedStats = updateStats(currentPlayer, dataForStats)

    return [pointsToAddToPlayer, updatedStats, currentPlayerTotalPoints + tempPoints]


def getKey(item):
    return item[1]


def printResults(players):

    playersToPrint = sorted(players, key=getKey)

    t = PrettyTable(['Pos', 'Name', 'Score'])

    pos = 1
    for ad in range(0, len(players)):
        t.add_row([pos, playersToPrint[ad][0], str(playersToPrint[ad][1])])
        pos = pos + 1

    print ("\n")
    print (t)
    print ("\n")


def printStatsForPlayer(players):

    playersToPrint = sorted(players, key=getKey)

    statsTable = PrettyTable(['', 'Name', 'Score', 'Average', 'Total throws', 'Time Played'])

    pos = 1

    for i in range(0, len(players)):

        currentStatsForPlayer = players[i][2]
        name = players[i][0]
        score = players[i][1]
        numberOfThrows = currentStatsForPlayer["throws"]
        statsTable.add_row([pos, name, score, int(round(currentStatsForPlayer["average"]) * 3), 
	numberOfThrows,time.strftime("%H:%M:%S", time.gmtime(int(currentStatsForPlayer["timePlayed"])))])

        pos = pos + 1

    print ("\n")
    print (statsTable)
    print ("\n")

def runMainProgram():
    print ("\nWelcome to dart calculator program!\n")

    # Initial operations before the actual game starts
    numberOfPlayer = int(input("Enter number of players: "))

    players = []

    points = selectGame()

    # Statistics for a player
    playerStats = {"average": 0, "throws": 0, "timePlayed": 0}

    curPlayerIndex = 0
    totalPoints = 0

    # Take players names as well as create a array of players
    for i in range(0, numberOfPlayer):
        playerName = takeUsersNames(numberOfPlayer, i)
        # Create an array for single player
        singlePlayer = [playerName, points, playerStats, totalPoints]
        players.append(singlePlayer)

    print ("\n")

    start_time = time.time()

    while True:
        # nextPlayer = False

        # Reset counter when loop went through all players
        if curPlayerIndex >= len(players):
            curPlayerIndex = 0

        currentPlayer = players[curPlayerIndex]

        gameInProgress = calcPoints(currentPlayer, points)

        if gameInProgress[0] == True:
            currentPlayer[2] = gameInProgress[1]
            currentPlayer[3] = gameInProgress[2]
            printResults(players)
            curPlayerIndex = curPlayerIndex + 1

        elif gameInProgress[0] == False:
            currentPlayer[2] = gameInProgress[1]
            currentPlayer[3] = gameInProgress[2]
            break
        else:
            # Update points for a player after 3 throws and increase a player index
            currentPlayer[1] = gameInProgress[0]
            currentPlayer[2] = gameInProgress[1]
            currentPlayer[3] = gameInProgress[2]
            printResults(players)
            curPlayerIndex = curPlayerIndex + 1


    elapsed_time = time.time() - start_time

    print ("\n                                --------- Winner ---------       {}\n".format(currentPlayer[0]))

    printStatsForPlayer(players)

    print (               "\nTotal time for a game: {} \n".format(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))


runMainProgram()

# TODO average for all players at the end for 3 shoots. All possibilities for
