class Player:

    cardsAvail = []                                                                 # Cards availiable in player hands

    def __init__(self):
        self.cardsAvail = []

    def takeCardfromDeck(self, card):                                               # To take cards form deck
        self.cardsAvail.append(card)

    def makeTurn(self, n):                                                          # To make turn with card "n" form cardsAvial[]
        selectedCard = self.cardsAvail[n]
        del self.cardsAvail[n]
        return selectedCard

    # def getPlayerCards(self, n=0):                                      # Do display availiable cards
    #     return self.cardsAvail[n:len(self.cardsAvail)]
    #
    def getPlayerCards(self, begin=0, end=False):
        if end is False:
            end = len(self.cardsAvail)                                    # Do display availiable cards
        return self.cardsAvail[begin:end]

def makePlayer(card1, card2, card3, card4):                                         # Player constructor
    player = Player()
    player.cardsAvail.append(card1)
    player.cardsAvail.append(card2)
    player.cardsAvail.append(card3)
    player.cardsAvail.append(card4)
    return player
