class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit} ({self.value})"

    def __int__(self):
        return self.value
    
    def __add__(self, other):
        return int(self) + int(other)