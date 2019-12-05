class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def __gt__(self, other):
        rank1 = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        if self.rank1 > other.rank1:
            return True
        elif other.rank1 > self.rank1:
            return False
        else:
            suit1 = [ "clubs","diamond", "hearts", "spades" ]
            suit2 = self.index(self.suit1)
            suit3 = self.index(other.suit1)
            if self.suit > other.suit:
                return True
            else:
                return False



    def __str__(self):
        values = ["Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        return  values[self.rank-1]+ " of " + self.suit