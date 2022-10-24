#
'''
The deck is divided evenly among the players, giving each a down stack. 
In unison, each player reveals the top card of their deck—this is a "battle"—and the player 
with the higher card takes both of the cards played and moves them to their stack. 
Aces are high, and suits are ignored.
'''
#
from cards import CardDeck
import matplotlib.pyplot as plt
import numpy as np
import PIL
import matplotlib
plt.style.use('ggplot')
matplotlib.use( 'tkagg' )

cards = CardDeck()
deck = cards.makeDeck()
shuffled_deck = cards.shuffleDeck()

player1_deck = []
player2_deck = []

sims_arr = []
monte_sim_runs =1000


for i in range(0,monte_sim_runs):
    for i in range(0,len(shuffled_deck)):
        if(i%2):
            player2_deck.append(shuffled_deck[i])
        else:
            player1_deck.append(shuffled_deck[i])
    turns = 0
    while(len(player1_deck) >= 2 or len(player2_deck) >= 2):
        try:
            if(player1_deck[1][0] > player2_deck[1][0]):
                player1_deck.append(player2_deck[1])
                player2_deck.pop(1)
            if(player2_deck[1][0] > player1_deck[1][0]):
                player2_deck.append(player1_deck[1])
                player1_deck.pop(1)
            if(player1_deck[1][0] == player2_deck[1][0]):
                player1_deck.pop(1)
                player2_deck.pop(1)
            turns += 1
            #  print("Turn :" + str(turns))
        except IndexError:
            sims_arr.append(turns)
            #  print('Ended the run')
            break

x_data = np.arange(0,max(sims_arr))
n_bins = 20

plt.hist(sims_arr)
plt.show()
