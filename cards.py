import random
import itertools

class CardDeck():
    rank = []
    suit = []
    deck = []
    def __init__(self):
        self.suit = ['Diamond','Club','Heart','Spade']
        self.rank = ['2','3','4','5','6','7','8','9','10','11','12','13','14']

    def makeDeck(self):
        self.deck = list(itertools.product(self.rank,self.suit))
        return self.deck
    
    def shuffleDeck(self):
        shuffled_deck = self.deck
        random.shuffle(shuffled_deck)
        return shuffled_deck



