
class AnagramChecker:
    def __init__(self,text_file):
        self.text_file = text_file

        with open(text_file, "r") as f:
            self.word_list = [word.strip().lower() for word in f]

    def is_valid_word(self, word):
        return word.isalpha()

    def is_anagram(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()

        return word1 != word2 and sorted(word1) == sorted(word2)

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []

        if not self.is_valid_word(word):
            return anagrams

        for i in self.word_list:
            if self.is_anagram(word, i):
                anagrams.append(i)

        return anagrams