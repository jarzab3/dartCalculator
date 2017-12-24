import datetime

print ("Welcome to dart calculator program!\n")

numberOfPlayer = int(input("Enter number of players: "))
points = int(input("Total points for game (301, 501, ...): "))

players  = []

def takeUsersNames(numberOfPlayer):
    while True:
        try:
            query = str(i + 1) + " player name? "
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
            # better try again... Return to the start of the loop

            continue

        else:
            return [userInput, points]

for i in range(0, numberOfPlayer):
    playersDetails = takeUsersNames(numberOfPlayer)
    players.append(playersDetails)

print ("\n")


def takeUsersInput(playersName):
    pointsInput = 0
    while True:
        try:
            playerFormatted = "Input points for player " + playersName + ": "
            pointsInput = int(input(playerFormatted))
        except ValueError:
            if not isinstance(points, int):
                print("Please input a integer")
            else:
                print("Incorrect input, please try again")
            # better try again... Return to the start of the loop

            continue

        else:
            return pointsInput

def calcPoints(curPlayerIndex, inPoints):

    findedPlayerPoints =  players[curPlayerIndex][1]
    findedPlayerName =  players[curPlayerIndex][0]

    check = (findedPlayerPoints - inPoints)

    if check < 0:
        print ("-----------------------------  Your points are not counted in!")
        return True

    elif check != 0:
        players[curPlayerIndex][1] = findedPlayerPoints - inPoints
        return True
    else:
        # endTime = datetime.datetime.now().time()
        print ("---------Wins--------- {}".format(findedPlayerName))
        return False

curPlayerIndex =  0


while True:
    breaker = False

    if curPlayerIndex >= len(players):
        curPlayerIndex = 0

    currentPlayer = players[curPlayerIndex]

    for x in range(0, 3):
        if currentPlayer[1] < 170:
            print ("-----------------------------  Close to win, your points are: {}".format(currentPlayer[1]))
        # playerFormatted = "Input points for player " + currentPlayer[0] + ": "
        # currentPoints1 = int(input(playerFormatted))
        currentPoints = takeUsersInput(currentPlayer[0])
        if currentPoints == 999:
            print ("You need to throw better")
            break
        else:
            gameInProgress = calcPoints(curPlayerIndex, currentPoints)
            if gameInProgress != True:
                breaker = True
                break

    curPlayerIndex = curPlayerIndex + 1

    if breaker:
        break

    allPlayersInfo = ""

    count = 0
    for ad in range(0, len(players)):

        if count == len(players) - 1:
            lastBit = False
        else:
            lastBit = True

        allPlayersInfo = allPlayersInfo + players[ad][0]
        if lastBit:
            allPlayersInfo =  allPlayersInfo + " = " + str(players[ad][1]) + "  |  "
        else:
            allPlayersInfo = allPlayersInfo + " = " + str(players[ad][1])

        count += 1

    print ("\nCurrent points for players: " + allPlayersInfo + "\n")
    print ("\n")

