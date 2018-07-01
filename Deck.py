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
    currentCardType = ""
    cardsOnTable = []

    def __init__(self):
        random.shuffle(self.cardsDeck)

    def putCardOnTable(self, card):
        self.currentCard = card
        self.cardsOnTable.append(card)
        self.currentSuit = self.currentCard[-1:]
        self.currentCardType = self.currentCard[0:-1]

    def giveCard(self):
        if (len(self.cardsDeck) == 0):
            self.cardsDeck = self.cardsOnTable[:-1]
            self.cardsOnTable = self.cardsOnTable[len(self.cardsOnTable)-1:]
            self.shuffleDeck()
        i = random.randint(0, len(self.cardsDeck)-1)
        newCard = self.cardsDeck[i]
        del self.cardsDeck[i]
        return newCard

    def shuffleDeck(self):
        random.shuffle(self.cardsDeck)

    def setNewCard(self, card):
        self.currentCard = card

    def getCurrentCardOnTable(self):
        return self.currentCard

    def getAllCardsOnTable(self):
        return self.cardsOnTable

    def setNewSuit(self, suit):
        self.currentSuit = suit

    def getCurrentSuit(self):
        return self.currentSuit

    def getCurrentCardType(self):
        return self.currentCardType

    def getDeckSize(self):
        return len(self.cardsDeck)

    def getDeckArray(self):
        return self.cardsDeck
