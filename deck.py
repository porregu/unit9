from card import *
import random

class Deck:

    def __init__(self):
        self.cards = []
        for suit in [ "clubs","diamond", "hearts", "spades" ]:
            for rank in range (1,14):
                new_card = Card(rank, suit)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()