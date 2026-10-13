import random

class Card:
    """Represents an individual playing card."""
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    """Represents a deck of 52 playing cards."""
    
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        self._reset_deck()

    def _reset_deck(self):
        """Generates a complete standard 52-card set."""
        self.cards = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]

    def shuffle(self):
        """Ensures the deck has all 52 cards and rearranges them randomly."""
        if len(self.cards) != 52:
            self._reset_deck()
        random.shuffle(self.cards)

    def deal(self):
        """Deals and removes a single card from the deck."""
        if not self.cards:
            raise ValueError("All cards have been dealt. Cannot deal from an empty deck.")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"


# --- Example Usage ---
if __name__ == "__main__":
    deck = Deck()
    print("Initial deck:", deck)  # Output: Deck of 52 cards

    # Shuffle the full deck
    deck.shuffle()

    # Deal a single card
    dealt_card = deck.deal()
    print("Dealt card:", dealt_card)  # Output e.g., "K of Spades"
    print("Remaining cards:", len(deck))  # Output: 51

    # Shuffling again restores all 52 cards
    deck.shuffle()
    print("After re-shuffling:", len(deck))  # Output: 52