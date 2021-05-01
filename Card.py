class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['jack', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit = 0, rank = 0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def compare(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank == 1 and other.rank == 14:
            if self.rank > other.rank: return -1
            if self.rank < other.rank: return 1
        elif self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        return 0

    def __eq__(self, other):
        return self.compare(other) == 0

    def __le__(self, other):
        return self.compare(other) <= 0

    def __ge__(self, other):
        return self.compare(other) >= 0

    def __gt__(self, other):
        return self.compare(other) > 0

    def __lt__(self, other):
        return self.compare(other) < 0

    def __ne__(self, other):
        return self.compare(other) != 0

    #def __add__(self, other):
    #    return self.compare(other) + 0