# game related imports
from deck import Deck
from manager import Manager
from hand import Hand

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

# welcome methods
print("Welcome to BlackJack game!")
print("Controls: h - hit, s - stand")

# while both players are playing
while player_hand.is_playing or dealer_hand.is_playing:
    # show the details of either hands
    print(f"Dealer's hand {int(dealer_hand)}: \n -{dealer_hand}")
    print(f"Your hand {int(player_hand)}: \n -{player_hand}")

    # if the players still plays
    # check out for his input
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