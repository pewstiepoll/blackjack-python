from functools import reduce

class Hand:
    def __init__(self):
        self.cards = []
        self.is_playing = True
        pass

    def hit(self, card):
        self.cards.append(card)

    def stand(self):
        self.is_playing = False

    def get_value(self):
        return reduce(lambda x, y: int(x) + int(y), self.cards)

    def __int__(self):
        return self.get_value()

    def __str__(self):
        return "\n -".join([str(card) for card in self.cards])
