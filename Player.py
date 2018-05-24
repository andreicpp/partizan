from Deck import Deck
mainDeck = Deck()

class Player:

    cardsAvail = []             # Cards availiable in player hands

    def __init__(self):
        self.cardsAvail = []

    def takeCard(self):         # To take cards form deck
        x=10

    def passTurn(self):         # To pass turn
        x=10

    def makeTurn(self, n):      # To make turn with card "n" form cardsAvial[]
        x=10

    def showCards(self):        # Do display availiable cards
        x=10

def makePlayer():
    player = Player()
    for i in range (0, 4):
        player.cardsAvail.append(mainDeck.giveCard())
    return player

player1 = makePlayer()
player2 = makePlayer()
player3 = makePlayer()

print(player1.cardsAvail)
print(player2.cardsAvail)
print(player3.cardsAvail)
print(mainDeck.cardsDeck)
