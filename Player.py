from Deck import Deck

class Player:

    mainDeck = Deck()

    cardsAvail = []             # Cards availiable in player hands

    def __init__(self):
        self.cardsAvail = []

    def takeCard(self):         # To take cards form deck
        self.cardsAvail.append(Player.mainDeck.giveCard())

    def passTurn(self):         # To pass turn
        x=10

    def makeTurn(self, n):      # To make turn with card "n" form cardsAvial[]
        selectedCard = self.cardsAvail[n]
        del self.cardsAvail[n]
        return selectedCard

    def showCards(self):        # Do display availiable cards
        return self.cardsAvail

def makePlayer():
    player = Player()
    for i in range (0, 4):
        player.cardsAvail.append(Player.mainDeck.giveCard())
    return player

# player1 = makePlayer()
# player2 = makePlayer()
# #player3 = makePlayer()
# player1.takeCard()
# player1.cardsAvail += ["ss", "ss1", "ss2"]
#
# print(player1.showCards())
# print(player2.showCards())
# o = player1.makeTurn(2)
# print(player1.showCards(), o)
