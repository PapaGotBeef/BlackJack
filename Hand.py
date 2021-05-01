from Deck import Deck
from Card import Card

class Hand(Deck):
    pass
    def __init__(self, name = ''):
        self.cards = []
        self.name = name
    def add(self,card):
        self.cards.append(card)

    def __str__(self):
        string = self.name + "'s hand"
        if self.is_empty():
            string += ' is empty\n'
        else:
            string +=' contains\n'
        return string + Deck.__str__(self)
