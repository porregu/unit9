class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __gt__(self, other):
        rank1 = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        if self.rank > other.rank:
            return True
        elif other.rank > self.rank:
            return False
        else:
            suit1 = [ "clubs","diamond", "hearts", "spades" ]
            suit2 = suit1.index(self.suit)
            suit3 = suit1.index(other.suit)
            if self.suit > other.suit:
                return True
            else:
                return False



    def __str__(self):
        values = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        return  values[self.rank-1]+ " of " + self.suit