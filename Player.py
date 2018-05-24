class Player:

    cardsAvail = []                                                                 # Cards availiable in player hands

    def __init__(self):
        self.cardsAvail = []

    def takeCardfromDeck(self, card):                                               # To take cards form deck
        self.cardsAvail.append(card)

    def passTurn(self):                                                             # To pass turn
        x=10

    def makeTurn(self, n):                                                          # To make turn with card "n" form cardsAvial[]
        selectedCard = self.cardsAvail[n]
        del self.cardsAvail[n]
        return selectedCard

    def showCards(self):                                                            # Do display availiable cards
        return self.cardsAvail

def makePlayer(card1, card2, card3, card4):                                         # Player constructor
    player = Player()
    player.cardsAvail.append(card1)
    player.cardsAvail.append(card2)
    player.cardsAvail.append(card3)
    player.cardsAvail.append(card4)
    return player
