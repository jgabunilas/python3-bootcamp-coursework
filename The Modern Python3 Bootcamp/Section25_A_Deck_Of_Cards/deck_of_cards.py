import random


# Card class
class Card:

        # Initialize the card with suit and value
        def __init__(self, suit, value):
                self.suit = suit
                self.value = value

        # Representation function that reports the value and suit of the card
        def __repr__(self):
                return f"{self.value} of {self.suit}"

# Deck class
class Deck:

        # Initialize the deck with 52 cards
        def __init__(self):
                cards_list = []
                suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
                values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
                for suit in suits:
                        for value in values:
                                cards_list.append(Card(suit, value))
                self.cards = cards_list

        # def __repr__(self):



# card = Card("hearts", "2")
# print(card)

deck1 = Deck()
print(deck1.cards)
print(len(deck1.cards))