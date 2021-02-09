import random


# Card class
class Card:

        # Initialize the card with suit and value
        def __init__(self, suit, value):
                self.suit = suit
                self.value = value

        # Representation function that reports the value and suit of the card
        def __repr__(self):
                return "{} of {}".format(self.value, self.suit)

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
                return "Deck of {} cards".format(self.count())


        # Defining a _deal method that removes at most the number of cards provided to the deck
        def _deal(self, cards_to_deal):
                # First check to ensure there are at least as many cards left in the deck as the number of cards to be dealt. If there are, remove the number of cards from the deck equal to the number of cards to be dealt
                if cards_to_deal <= self.count():
                        cards_dealt = []
                        for num in range(cards_to_deal):
                                cards_dealt.append(self.cards.pop())
                                # print(self.count())
                        return cards_dealt
                # If there are fewer cards than need to be dealt, deal the rest of the cards (if there are any) and then raise the ValueError stating that all cards have been dealt
                else:
                        if self.count() > 0:
                                for num in range(cards_to_deal - self.count()):
                                        self.cards.pop()
                                        # print(self.count())
                        raise ValueError("All cards have been dealt")

                                
        
        # Defining a count method that returns the number of cards in the deck
        def count(self):
                return len(self.cards)

        # Defining a shuffle method to shuffle a full deck of cards
        def shuffle(self):
                return random.shuffle(self.cards)

        # Define a deal_card function that uses the _deal method to deal a single card from the deck. This involves calling the _deal method with a cards_to_deal value of 1
        def deal_card(self):
                return self._deal(1)[0]

        # Define a deal_hand function that uses the _deal method to deal a list of cards equal to the number entered
        def deal_hand(self, cards_to_deal):
                return self._deal(cards_to_deal)
        


# card = Card("hearts", "2")
# print(card)

# deck1 = Deck()
# # print(deck1.cards)
# # # print(len(deck1.cards))
# # print(deck1.count())

# # print(deck1)
# # print(deck1._deal(5))
# # print(deck1)

# deck1.shuffle()
# # print(deck1)
# # card1 = deck1.deal_card()
# # print(card1)
# # print(deck1)

# # print(deck1._deal(100))
# print(deck1)
# print(deck1.deal_hand(5))
# print(deck1)

d = Deck()
# d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()