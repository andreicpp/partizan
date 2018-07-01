from Player import Player
from Deck import Deck
from PlayersStats import PlayersStats

PLAYERNUM = 4

deck = Deck()

game = PlayersStats(PLAYERNUM, deck.cardsDeck[0:-len(deck.cardsDeck)+PLAYERNUM*4])  # Give cards to players (at the begin 4 to each)
deck.cardsDeck = deck.cardsDeck[-len(deck.cardsDeck)+PLAYERNUM*4:]

deck.putCardOnTable (deck.giveCard())
#game.setCurrentSuit(deck.getCurrentCardOnTable()[-1:])


def checkCurrentCardOnTable(card):

    if ("6" in card[0]):
        if (game.getCurrentPlayer() == 0): i = PLAYERNUM-1;
        else : i = game.getCurrentPlayer()-1
        game.playersArray[i].takeCardfromDeck(deck.giveCard())
        if (game.howMuchPlayers() == 2): game.nextPlayerTurn()
        return

    if ("7" in card[0]):
        if (game.getCurrentPlayer() == PLAYERNUM-1): i = 0
        else : i = game.getCurrentPlayer()+1
        for j in range (0, 2):
            game.playersArray[i].takeCardfromDeck(deck.giveCard())
        if (PLAYERNUM*4 + deck.getDeckSize() + 2 + 1 == 36):                         # if "7" - to make aditional turn in firs round
            game.nextPlayerTurn()
        game.nextPlayerTurn()
        return

    if ("9d" in card):
        if (game.getCurrentPlayer() == PLAYERNUM-1): i = 0
        else : i = game.getCurrentPlayer()+1
        for j in range (0, 5):
            game.playersArray[i].takeCardfromDeck(deck.giveCard())
        game.nextPlayerTurn()
        return

    if ("A" in card[0]):
        game.nextPlayerTurn()
        return

def checkIfNotEnd():
    for i in range (0, PLAYERNUM):
        if (len(game.playersArray[i].getPlayerCards()) == 0):
            return False
    return True

def changeSuit(suit):
    game.setCurrentSuit(suit)

def isGoodCard(chosenCard):
    if (chosenCard[0:-1] == 'J'):
        return True
    if (chosenCard[-1:] == deck.getCurrentSuit()):
        return True
    if (chosenCard[0:-1] == deck.getCurrentCardType()):
        return True
    return False

while checkIfNotEnd():

    checkCurrentCardOnTable(deck.getCurrentCardOnTable())

    for i in range(0, PLAYERNUM):
        print(game.playersArray[i].getPlayerCards())

    print ("current:", deck.getCurrentCardOnTable())
    print("current card:", deck.getCurrentCardType())
    print ("current suit:", deck.getCurrentSuit())
    print("on table:",deck.getAllCardsOnTable())

    print ("No:", game.getCurrentPlayer()+1, ":")
    print (game.playersArray[game.getCurrentPlayer()].getPlayerCards())

######################### PLAYER CHOOSE CARD FOR TURN ###################################
    while (True):
        chosenCard = input("CHOUSE NUMBER THE CARD (\"Press enter\" if no card):")

        if (chosenCard != '' and isGoodCard(''.join(game.playersArray[game.getCurrentPlayer()].getPlayerCards(int(chosenCard)-1, int(chosenCard))))):
                deck.putCardOnTable(game.playersArray[game.getCurrentPlayer()].makeTurn(int(chosenCard)-1))
                if (deck.getCurrentCardType() == 'J'):
                    newSuit = input("CHANGE SUIT:")
                    deck.setNewSuit(newSuit)
                break
        if (chosenCard == ''):
            game.playersArray[game.getCurrentPlayer()].takeCardfromDeck(deck.giveCard())
            print ("No:", game.getCurrentPlayer()+1, ":")
            print (game.playersArray[game.getCurrentPlayer()].getPlayerCards())
            while (True):
                chosenCard = input("CHOUSE NUMBER THE CARD (\"Press enter\" if no card):")
                if (chosenCard != '' and isGoodCard(''.join(game.playersArray[game.getCurrentPlayer()].getPlayerCards(int(chosenCard)-1, int(chosenCard))))):
                    deck.putCardOnTable(game.playersArray[game.getCurrentPlayer()].makeTurn(int(chosenCard)-1))
                    if (deck.getCurrentCardType() == 'J'):
                        newSuit = input("CHANGE SUIT:")
                        deck.setNewSuit(newSuit)
                    break
                if (chosenCard == ''):
                    break
                print ("wrong card")
            break
        print ("wrong card")

    game.nextPlayerTurn()
################################ END OF BLOCK #########################################
