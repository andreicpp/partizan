from Player import makePlayer
import random

class PlayersStats:

    numberOfPlayers = 0
    currentPlayer = 0
    playersScore = []
    playersArray = []

    def __init__ (self, num, cardArr):
        self.numberOfPlayers = num
        self.currentPlayer = random.randint(0,num-1)
        j=0
        for i in range (0, num):
            self.playersScore += [0]
            self.playersArray.append(makePlayer(cardArr[j], cardArr[j+1], cardArr[j+2], cardArr[j+3]))
            j = j+4

    def whoIsCurrentPlayer(self):
        return self.currentPlayer
