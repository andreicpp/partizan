from Player import Player

class Table:

    cardsOnTable = []
    currnetCard = ""

    def discardPile(self):
        Player.mainDeck.usedCards += self.cardsOnTable
        self.cardsOnTable = []

    def abbadonDefense(self, Player):
        Player.cardsAvail += self.cardsOnTable
        self.cardsOnTable = []

    def putCardOnTable(self, card):
        self.cardsOnTable += card
        self.currnetCard = card

# print (Player.mainDeck.cardsDeck)
