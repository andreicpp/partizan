import random

class Deck:

    cardsDeck = ["6c", "6d", "6h", "6s",
                 "7c", "7d", "7h", "7s",
                 "8c", "8d", "8h", "8s",
                 "9c", "9d", "9h", "9s",
                 "10c", "10d", "10h", "10s",
                 "Jc", "Jd", "Jh", "Js",
                 "Qc", "Qd", "Qh", "Qs",
                 "Kc", "Kd", "Kh", "Ks",
                 "Ac", "Ad", "Ah", "As"]
    currnetCard = ""
    usedCards = []
    cardsOnTable = []

    def __init__(self):
        random.shuffle(self.cardsDeck)
        self.currnetCard = self.cardsDeck[0]
        self.cardsOnTable = self.cardsDeck[0]
        del self.cardsDeck[0]

    def discardPile(self):
        self.usedCards = self.cardsOnTable
        self.cardsOnTable = []
        self.currnetCard = ""

    def abbadonDefense(self):
        cards = self.cardsOnTable
        self.cardsOnTable = []
        self.currnetCard = ""
        return cards

    def putCardOnTable(self, card):
        self.cardsOnTable += card
        self.currnetCard = card

    def giveCard(self):
        if (len(self.cardsDeck) == 0):
            self.cardsDeck = self.usedCards
            self.usedCards = []
            self.shuffleDeck
        i = random.randint(0, len(self.cardsDeck)-1)
        newCard = self.cardsDeck[i]
        del self.cardsDeck[i]
        return newCard

    def shuffleDeck(self):
        random.shuffle(self.cardsDeck)

    def showCurrentCardOnTable(self):
        return self.currnetCard

    def showAllCardsInDeck(self):
        return self.cardsDeck

    def showAllUsedCards(self):
        return self.usedCards
