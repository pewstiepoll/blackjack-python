from random import shuffle
from card import Card

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

    @staticmethod
    def get_top_card(deck):
        return deck.cards.pop()

