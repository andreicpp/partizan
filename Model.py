from Player import Player
from Deck import Deck
from PlayersStats import PlayersStats

PLAYERNUM = 4

deck = Deck()

game = PlayersStats(PLAYERNUM, deck.cardsDeck[0:-len(deck.cardsDeck)+PLAYERNUM*4])  # Give cards to players (at the begin 4 to each)
deck.cardsDeck = deck.cardsDeck[-len(deck.cardsDeck)+PLAYERNUM*4:]
deck.putCardOnTable (game.playersArray[game.currentPlayer].getPlayerCards(3))
game.playersArray[game.currentPlayer].makeTurn(3)

def checkCurrentCard(card):

    if ("6" in card[0]):
        if (game.currentPlayer == 0): i = PLAYERNUM-1;
        else : i = game.currentPlayer-1
        game.playersArray[i].takeCardfromDeck(deck.giveCard())

    if ("7" in card[0]):
        if (game.currentPlayer == PLAYERNUM-1): i = 0
        else : i = game.currentPlayer+1
        for j in range (0, 2):
            game.playersArray[i].takeCardfromDeck(deck.giveCard())

    if ("9d" in card[0]):
        if (game.currentPlayer == PLAYERNUM-1): i = 0
        else : i = game.currentPlayer+1
        for j in range (0, 5):
            game.playersArray[i].takeCardfromDeck(deck.giveCard())


#deck.currentCard = "9"

# kl = 0
# while(kl<1):
#     kl+=1
checkCurrentCard(deck.getCurrentCardOnTable())


print (deck.getCurrentCardOnTable())
for i in range(0, PLAYERNUM):
    print(game.playersArray[i].getPlayerCards())
#print (deck.getAllCardsInDeck())
