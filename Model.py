from Player import Player
from Deck import Deck
from PlayersStats import PlayersStats

PLAYERNUM = 4

deck = Deck()

game = PlayersStats(PLAYERNUM, deck.cardsDeck[0:-len(deck.cardsDeck)+PLAYERNUM*4])  # Give cards to players (at the begin 4 to each)
deck.cardsDeck = deck.cardsDeck[-len(deck.cardsDeck)+PLAYERNUM*4:]
#deck.putCardOnTable (game.playersArray[game.currentPlayer].getPlayerCards(3))
#game.playersArray[game.currentPlayer].makeTurn(3)
#game.setCurrentSuit(deck.getCurrentCardOnTable()[0][len(deck.getCurrentCardOnTable()[0])-1])
deck.putCardOnTable (deck.giveCard())
game.setCurrentSuit(deck.getCurrentCardOnTable()[-1:])


def checkCurrentCardOnTable(card):

    if ("6" in card[0]):
        if (game.getCurrentPlayer() == 0): i = PLAYERNUM-1;
        else : i = game.getCurrentPlayer()-1
        game.playersArray[i].takeCardfromDeck(deck.giveCard())
        if (game.howMuchPlayers() == 2): game.nextPlayerTurn()

    if ("7" in card[0]):
        if (game.getCurrentPlayer() == PLAYERNUM-1): i = 0
        else : i = game.getCurrentPlayer()+1
        for j in range (0, 2):
            game.playersArray[i].takeCardfromDeck(deck.giveCard())
        game.nextPlayerTurn()

    if ("9d" in card):
        if (game.getCurrentPlayer() == PLAYERNUM-1): i = 0
        else : i = game.getCurrentPlayer()+1
        for j in range (0, 5):
            game.playersArray[i].takeCardfromDeck(deck.giveCard())
        game.nextPlayerTurn()

    if ("A" in card[0]):
        game.nextPlayerTurn()

def checkIfEnd():
    for i in range (0, PLAYERNUM):
        if (len(game.playersArray[i].getPlayerCards()) == 0):
            return True
    return False


print (game.getCurrnetSuit())

checkCurrentCardOnTable(deck.getCurrentCardOnTable())


print (deck.getCurrentCardOnTable())
for i in range(0, PLAYERNUM):
    print(game.playersArray[i].getPlayerCards())

print (game.getCurrentPlayer())
#print (deck.getAllCardsInDeck())
