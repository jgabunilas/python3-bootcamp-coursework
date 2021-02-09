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
                # Define the cards attribute with all 52 instances of Card
                self.cards = cards_list
        
       
        # Defining a __repr__ method that returns how many cards are in the deck. Calls the count method.    
        def __repr__(self):
                return f"Deck of {self.count()} cards"

        # Defining a count method that returns the number of cards in the deck
        def count(self):
                return len(self.cards)

        # Defining a _deal method that removes at most the number of cards provided to the deck
        def _deal(self, cards_to_deal):
                # First check to ensure there are at least as many cards left in the deck as the number of cards to be dealt. If there are, remove the number of cards from the deck equal to the number of cards to be dealt
                if cards_to_deal <= self.count():
                        for num in range(cards_to_deal):
                                self.cards.pop()
                                print(self.count())
                # If there are fewer cards than need to be dealt, deal the rest of the cards then raise the ValueError stating that all cards have been dealt
                else:
                        for num in range(cards_to_deal - self.count()):
                                self.cards.pop()
                                print(self.count())
                        return ValueError("All cards have been dealt")
        





# card = Card("hearts", "2")
# print(card)

deck1 = Deck()
# print(deck1.cards)
# # print(len(deck1.cards))
# print(deck1.count())
print(deck1)
print(deck1._deal(5))
print(deck1)
