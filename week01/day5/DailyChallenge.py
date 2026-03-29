#Challenge 1: Letter Index Dictionary
#Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).

#    * If it is, append the current index to the list associated with that key.
#    * If it is not, create a new key-value pair in the dictionary.


user_string = input("Type a word: ")
char_str_index = {}

for i, char in enumerate(user_string):
    if char in char_str_index:
       char_str_index[char].append(i)
    else:
        char_str_index[char] = [i]

print(char_str_index)