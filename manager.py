from random import shuffle
from card import Card

"""
    Manager class does all deck related manipulations:
     - fill the given deck
     - shuffle the given deck
     - receive top card of the deck
"""
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

    """
        Fill the given deck with cards
    """
    @staticmethod
    def fill_deck(deck):
        for suit in Manager.suits:
            for (rank, value) in Manager.ranks.items():
                deck.add_card(Card(suit, rank, value))

    """
        Randomly shuffle the given deck
    """
    @staticmethod
    def shuffle_deck(deck):
        shuffle(deck.cards)

    """
        Returns the top card from the deck
    """
    @staticmethod
    def get_top_card(deck):
        return deck.cards.pop()

