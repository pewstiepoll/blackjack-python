from collections import namedtuple
from random import shuffle


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit} ({self.value})"


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return "\n".join(map(str, self.cards))


class Manager:
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11,
    }

    @staticmethod
    def fill_deck(deck):
        for suit in Manager.suits:
            for (rank, value) in Manager.ranks.items():
                deck.add_card(Card(suit, rank, value))

    @staticmethod
    def shuffle_deck(deck):
        shuffle(deck.cards)


# Create new deck
deck = Deck()

# Fill deck with cards
Manager.fill_deck(deck)

# Shuffle cards in deck
Manager.shuffle_deck(deck)
