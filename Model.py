from Player import Player
from Deck import Deck
from PlayersStats import PlayersStats

PLAYERNUM = 4

deck = Deck()

game = PlayersStats(PLAYERNUM, deck.cardsDeck[0:-len(deck.cardsDeck)+PLAYERNUM*4])  # Give cards to players (at the begin 4 to each)
deck.cardsDeck = deck.cardsDeck[-len(deck.cardsDeck)+PLAYERNUM*4:]

for i in range (0, PLAYERNUM):
    print (game.playersArray[i].showCards())

print (deck.showCurrentCardOnTable())
