from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        string = ''
        for i in range(len(self.cards)):
            string = string + ' ' * i + str(self.cards[i]) + "\n"
        return string


    def shuffle(self):
        import random
        rand = random.Random()
        rand.shuffle(self.cards)


    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False


    def pop(self):
        return self.cards.pop()


    def is_empty(self):
        return self.cards == []


    def deal(self, hands, num_cards):
        num_hands = len(hands)
        value = num_hands * num_cards
        for i in range(value):
            if self.is_empty():
                print("out of cards")
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)

