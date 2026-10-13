# Exercise 1: Quiz
"""
What is a class?
A class is a blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods) that all objects instantiated from it will share.

What is an instance?
An instance is a specific, concrete object created from a class blueprint in memory, containing its own distinct attribute values.

What is encapsulation?
Encapsulation is the bundling of data (attributes) and the methods that manipulate that data into a single class unit, while restricting direct access to internal state components to protect data integrity.

What is abstraction?
Abstraction is the concept of hiding complex internal implementation details and exposing only the essential interface needed to interact with the object.

What is inheritance?
Inheritance allows a child class to acquire the attributes and methods of a parent class, promoting code reuse, specialization, and logical hierarchy.

What is multiple inheritance?
Multiple inheritance occurs when a single subclass inherits directly from more than one parent class.

What is polymorphism?
Polymorphism enables objects of different classes to respond to the same method call in class-specific ways, allowing unified code execution across disparate types.

What is Method Resolution Order (MRO)?
Method Resolution Order (MRO) is the linear sequence Python follows to search for methods or attributes in a class hierarchy, especially when resolving conflicts in multiple inheritance (computed via the C3 Linearization algorithm).
"""

# Exercise 2: Deck of Cards Implementation
import random

class Card:
    """Represents an individual playing card with a suit and value."""
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    """Represents a standard 52-card playing deck."""
    
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        self._reset_deck()

    def _reset_deck(self):
        """Builds a complete 52-card set."""
        self.cards = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]

    def shuffle(self):
        """Ensures the deck has all 52 cards and randomly shuffles them."""
        if len(self.cards) != 52:
            self._reset_deck()
        random.shuffle(self.cards)

    def deal(self):
        """Deals a single card from the deck and removes it."""
        if not self.cards:
            raise ValueError("All cards have been dealt from the deck.")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"


# --- Example Usage ---
if __name__ == "__main__":
    deck = Deck()
    print(deck)  # Output: Deck of 52 cards

    # Shuffle the full deck
    deck.shuffle()

    # Deal a card
    card = deck.deal()
    print("Dealt card:", card)
    print("Remaining cards:", len(deck))  # Output: 51

    # Re-shuffling restores the deck to 52 cards
    deck.shuffle()
    print("Cards after re-shuffling:", len(deck))  # Output: 52