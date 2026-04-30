# Part 1 : Quizz

#What is a class? Blueprint for objects.
# What is an instance? An actual object created from a class.
# What is encapsulation? Concept of hiding data and allowing controlled access via methods.
# What is abstraction?Concept of hiding complexity and showing only essential functionality.
# What is inheritance? Allows a child class to use attributes and methods from a parent class.
# What is multiple inheritance? Child class inherits features from multiple parent classes
# What is polymorphism? When the same method name behaves different depending on the object name.
# What is method resolution order or MRO? The order that python searches through classes for methods.


# Part 2: Create a deck of cards class
import random as rnd

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.full_deck = [
            Card(suit, value)
            for suit in self.suits
            for value in self.values
        ]

    def shuffle(self):
        if len(self.full_deck) == 52:
            return rnd.shuffle(self.full_deck)
        else:
            print("there is les than 52 cards here")

    def deal(self):
        if len(self.full_deck) > 0:
            return self.full_deck.pop()
        return None

deck = Deck()

print("New deck created:")
print(deck.full_deck)
print(len(deck.full_deck))  # should be 52

print("\nShuffling deck...")
deck.shuffle()

print(deck.full_deck[:5])  # show first 5 cards after shuffle

print("\nDealing 3 cards...")
print(deck.deal())
print(deck.deal())
print(deck.deal())

print("\nCards left in deck:")
print(len(deck.full_deck))