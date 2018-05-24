from Player import makePlayer

class PlayersStats:

    numberOfPlayers = 0
    currentPlayer = 0
    playersScore = []
    playersArray = []

    def __init__ (self, num, cardArr):
        self.numberOfPlayers = num
        j=0
        for i in range (0, num):
            self.playersScore += [0]
            self.playersArray.append(makePlayer(cardArr[j], cardArr[j+1], cardArr[j+2], cardArr[j+3]))
            j = j+4

    def checkIfGoodCard(self, card):
        x=0
