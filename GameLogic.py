from Player import Player
from Player import makePlayer
from Table import Table
PLAYERNUM = 4

playerArray = []

class GameLogic:

    numberOfPlayers = 0
    currentPlayer = 0
    playersScore = []

    def __init__ (self, num):
        self.numberOfPlayers = num
        for i in range (0, num):
            self.playersScore += [0]


    def checkIfGoodCard(self, card):
        x=0



newGame = GameLogic(PLAYERNUM)

for i in range (0, PLAYERNUM):
    playerArray.append(makePlayer())

for i in range (0, PLAYERNUM):
    print (playerArray[i].showCards())
#print ([Player() for x in range(PLAYERNUM)])


#print (newGame.playersScore)
