import string
import re
from collections import Counter
from typing import Optional


class Text:
    """
    Class to analyze text data from a string or loaded directly from a file.
    """

    def __init__(self, text: str):
        self.text = text

    def _get_words(self) -> list[str]:
        """
        Helper method to extract normalized words.
        
        Splits text on whitespace, strips leading/trailing punctuation,
        and converts all tokens to lowercase for case-insensitive matching.
        """
        return [
            word.strip(string.punctuation).lower()
            for word in self.text.split()
            if word.strip(string.punctuation)
        ]

    # -------------------------------------------------------------------------
    # Part I Methods
    # -------------------------------------------------------------------------
    def word_frequency(self, word: str) -> int:
        """
        Step 2: Counts occurrences of a specific word in the text.
        
        Performs case-insensitive matching. Returns 0 if the word is not found.
        """
        words = self._get_words()
        return words.count(word.lower())

    def most_common_word(self) -> Optional[str]:
        """
        Step 3: Finds and returns the word with the highest frequency in the text.
        
        Returns None if the text contains no valid words.
        """
        words = self._get_words()
        if not words:
            return None

        counts = Counter(words)
        most_common, _ = counts.most_common(1)[0]
        return most_common

    def unique_words(self) -> list[str]:
        """
        Step 4: Returns a sorted list of unique normalized words present in the text.
        """
        words = self._get_words()
        return sorted(set(words))

    # -------------------------------------------------------------------------
    # Part II Class Method
    # -------------------------------------------------------------------------
    @classmethod
    def from_file(cls, file_path: str):
        """
        Step 5: Reads file content and returns a new Text instance.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return cls(content)


# ==============================================================================
# Bonus: Text Modification Class
# ==============================================================================
class TextModification(Text):
    """
    Subclass of Text providing text cleaning and normalization utilities.
    """

    STOP_WORDS = {
        "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
        "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
        "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
        "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during",
        "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't",
        "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
        "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i",
        "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's",
        "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself",
        "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
        "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
        "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such",
        "than", "that", "that's", "the", "their", "theirs", "them", "themselves",
        "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
        "they've", "this", "those", "through", "to", "too", "under", "until", "up",
        "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
        "weren't", "what", "what's", "when", "when's", "where", "where's", "which",
        "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would",
        "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
        "yourself", "yourselves"
    }

    def remove_punctuation(self) -> str:
        """
        Step 7: Removes punctuation from self.text using string.punctuation.
        """
        translator = str.maketrans("", "", string.punctuation)
        return self.text.translate(translator)

    def remove_stop_words(self) -> str:
        """
        Step 8: Removes common English stop words and surrounding punctuation.
        """
        words = self.text.split()
        filtered = []
        for word in words:
            clean_word = word.strip(string.punctuation)
            if clean_word.lower() not in self.STOP_WORDS and clean_word:
                filtered.append(clean_word)
        return " ".join(filtered)

    def remove_special_characters(self) -> str:
        """
        Step 9: Removes special characters (keeping alphanumeric and spaces) using regex.
        """
        return re.sub(r"[^a-zA-Z0-9\s]", "", self.text)


# ==============================================================================
# Test Execution
# ==============================================================================
if __name__ == "__main__":
    sample_phrase = "A good book has no ending. A good book is an endless journey!"

    print("--- Part I: Basic Text Analysis ---")
    t = Text(sample_phrase)

    print("Word Frequency ('good'):", t.word_frequency("good"))  # Output: 2
    print("Word Frequency ('python'):", t.word_frequency("python"))  # Output: 0
    print("Most Common Word:", t.most_common_word())  # Output: 'a' or 'good' or 'book'
    print("Unique Words Count:", len(t.unique_words()))
    print("Unique Words List (Sorted):", t.unique_words())

    print("\n--- Bonus: Text Modification ---")
    mod = TextModification("Hello, World! This is a test string with @special #characters and punctuation!")

    print("Original Text:\n ", mod.text)
    print("\n1. Remove Punctuation:\n ", mod.remove_punctuation())
    print("\n2. Remove Stop Words:\n ", mod.remove_stop_words())
    print("\n3. Remove Special Characters:\n ", mod.remove_special_characters())