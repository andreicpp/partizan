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
    currentCard = ""
    currentSuit = ""
    usedCards = []
    cardsOnTable = []


    def __init__(self):
        random.shuffle(self.cardsDeck)

    def discardPile(self):
        self.usedCards = self.cardsOnTable
        self.cardsOnTable = []
        self.currentCard = ""

    def abbadonDefense(self):
        cards = self.cardsOnTable
        self.cardsOnTable = []
        self.currentCard = ""
        return cards

    def putCardOnTable(self, card):
        self.currentCard = card
        self.cardsOnTable.append(card)
        self.currentSuit = self.currentCard[-1:]


    def giveCard(self):
        if (len(self.cardsDeck) == 0):
            self.cardsDeck = self.usedCards
            self.usedCards = []
            self.shuffleDeck
        i = random.randint(0, len(self.cardsDeck)-1)
        newCard = self.cardsDeck[i]
        del self.cardsDeck[i]
        return newCard

    def setCurrentCard(self, card):
        self.currentCard = card

    def shuffleDeck(self):
        random.shuffle(self.cardsDeck)

    def getCurrentCardOnTable(self):
        return self.currentCard

    def getAllCardsOnTable(self):
        return self.cardsOnTable

    def getAllUsedCards(self):
        return self.usedCards

    def getCurrentSuit(self):
        return self.currentSuit
