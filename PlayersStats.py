from Player import makePlayer
import random

class PlayersStats:

    numberOfPlayers = 0
    currentPlayer = 0                       # from 0 to N-1
    playersScore = [0,0,0,0]                       # score of each player
    playersArray = []                       #
    currentSuit = ""

    def __init__ (self, num, cardArr):
        self.numberOfPlayers = num
        self.currentPlayer = random.randint(0,num-1)
        j=0
        for i in range (0, num):
            self.playersScore += [0]
            self.playersArray.append(makePlayer(cardArr[j], cardArr[j+1], cardArr[j+2], cardArr[j+3]))
            j = j+4

    def nextPlayerTurn(self):
        if (self.currentPlayer == len(self.playersArray)-1):
            self.currentPlayer = 0
        else :
            self.currentPlayer += 1

    def setCurrentSuit(self, suit):
        self.currentSuit = suit

    def setPlayersScore(self, nr, score):
        if (nr<0):
            self.playersScore[self.numberOfPlayers-1] = score
        else:
            self.playersScore[nr] = score

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getCurrnetSuit(self):
        return self.currentSuit

    def getPlayersScore(self):
        return self.playersScore

    def howMuchPlayers(self):
        return self.numberOfPlayers
