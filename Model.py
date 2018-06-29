from Player import Player
from Deck import Deck
from PlayersStats import PlayersStats

PLAYERNUM = 4

deck = Deck()

game = PlayersStats(PLAYERNUM, deck.cardsDeck[0:-len(deck.cardsDeck)+PLAYERNUM*4])  # Give cards to players (at the begin 4 to each)
deck.cardsDeck = deck.cardsDeck[-len(deck.cardsDeck)+PLAYERNUM*4:]

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

def checkIfNotEnd():
    for i in range (0, PLAYERNUM):
        if (len(game.playersArray[i].getPlayerCards()) == 0):
            return False
    return True

def changeSuit(suit):
    game.setCurrentSuit(suit)





print (game.getCurrnetSuit())

checkCurrentCardOnTable(deck.getCurrentCardOnTable())


print (deck.getCurrentCardOnTable())
for i in range(0, PLAYERNUM):
    print(game.playersArray[i].getPlayerCards())

print (len(game.playersArray[0].getPlayerCards()))

while checkIfNotEnd():

    print ("PLAYER", game.getCurrentPlayer()+1, "TURN. CARDS:")
    print (game.playersArray[game.getCurrentPlayer()].getPlayerCards())

######################### PLAYER CHOOSE CARD FOR TURN ###################################
    chosenCard = input("CHOUSE NUMBER THE CARD (\"Press enter\" if no card):")
    if (chosenCard != ''):
        int(chosenCard)
        deck.putCardOnTable(game.playersArray[game.getCurrentPlayer()].makeTurn(int(chosenCard)-1))
        game.nextPlayerTurn()
    else:
        game.playersArray[game.getCurrentPlayer()].takeCardfromDeck(deck.giveCard())
        print ("PLAYER", game.getCurrentPlayer()+1, "TURN. CARDS:")
        print (game.playersArray[game.getCurrentPlayer()].getPlayerCards())
        chosenCard = input("CHOUSE NUMBER THE CARD (\"Press enter\" if no card):")
        if (chosenCard != ''):
            int(chosenCard)
            deck.putCardOnTable(game.playersArray[game.getCurrentPlayer()].makeTurn(int(chosenCard)-1))
        else:
            game.nextPlayerTurn()
################################ END OF BLOCK #########################################

    print (deck.getCurrentCardOnTable())
    print (deck.getCurrentSuit())

    for i in range (0, len(deck.cardsOnTable)):
        print(deck.cardsOnTable)
