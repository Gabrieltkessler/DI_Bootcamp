# Challenge 1: Sorting
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

words = input('type your words here: ')

word_list = words.split(",")
word_list = [word.strip() for word in word_list]
word_list.sort()

result = ",".join(word_list)

print(result)

# Challenge 2: Longest Word
# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.

def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
    
print(longest_word("This is an example sentence to return the longest word along with it's characters."))
print(longest_word("Another quick set of words to see what's up"))
print(longest_word("Final set of words but we will go as long as possible for this one to see if the code really works."))