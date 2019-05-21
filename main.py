from functools import reduce
from collections import namedtuple
from random import shuffle


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

    @staticmethod
    def get_top_card(deck):
        return deck.cards.pop()


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

# Create new deck
deck = Deck()

# Fill deck with cards
Manager.fill_deck(deck)

# Shuffle cards in deck
Manager.shuffle_deck(deck)

## Game starts here
player_hand = Hand()
dealer_hand = Hand()

# Fill hands
player_hand.hit(Manager.get_top_card(deck))
dealer_hand.hit(Manager.get_top_card(deck))
player_hand.hit(Manager.get_top_card(deck))
dealer_hand.hit(Manager.get_top_card(deck))


print("Welcome to BlackJack game!")
print("Controls: h - hit, s - stand")

while player_hand.is_playing or dealer_hand.is_playing:
    print(f"Dealer's hand {int(dealer_hand)}: \n -{dealer_hand}")
    print(f"Your hand {int(player_hand)}: \n -{player_hand}")

    if player_hand.is_playing:
        key = str(input("Key: "))

        if key.lower() == "h":
            # user hits
            card = Manager.get_top_card(deck)
            print(f"You hit {card}")
            player_hand.hit(card)
        elif key.lower() == "s":
            # user stands
            print("You stand.")
            player_hand.stand()
        else:
            # unrecognized command, continue
            continue

    # if dealer has less than 15 he hits
    # and stands if more
    if dealer_hand.is_playing and int(dealer_hand) < 15:
        card = Manager.get_top_card(deck)
        print(f"Dealer hits {card}")
        dealer_hand.hit(card)
    else:
        print("Dealer stands.")
        dealer_hand.stand()

    # if player overtakes
    if int(player_hand) > 21:
        player_hand.stand()
        dealer_hand.stand()
        print(f"You've reached {int(player_hand)} and lose.")

    # if dealer overtakes
    if int(dealer_hand) > 21:
        player_hand.stand()
        dealer_hand.stand()
        print(f"Dealer reached {int(dealer_hand)} and lose.")

# everyone stands
# time to get the winner
if int(player_hand) > int(dealer_hand) and int(player_hand) <= 21:
    print(f"You won with score: {int(player_hand)}")
elif int(player_hand) < int(dealer_hand) and int(dealer_hand) <= 21:
    print(f"Dealer won with score: {int(dealer_hand)}")