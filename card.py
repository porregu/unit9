class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __gt__(self, other):
        if self.rank > other.rank:
            return True
        elif other.rank > self.rank:
            return False
        #else:



    def __str__(self):
        values = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        return  values[self.rank-1]+ " of " + self.suit