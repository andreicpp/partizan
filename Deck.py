import random

class Deck:

    cardsDeck = ["7c", "7d", "7h", "7s",
                 "8c", "8d", "8h", "8s",
                 "9c", "9d", "9h", "9s",
                 "10c", "10d", "10h", "10s",
                 "Jc", "Jd", "Jh", "Js",
                 "Qc", "Qd", "Qh", "Qs",
                 "Kc", "Kd", "Kh", "Ks",
                 "Ac", "Ad", "Ah", "As"]

    def __init__(self):
        random.shuffle(self.cardsDeck)

    def shuffleDeck(self):
        random.shuffle(self.cardsDeck)

    def giveCard(self):
        #if (len(self.cardsDeck) == 0):
            #getTableDiscard
        i = random.randint(0, len(self.cardsDeck)-1)
        newCard = self.cardsDeck[i]
        del self.cardsDeck[i]
        return newCard
