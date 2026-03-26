#Challenge 1: Multiples of a Number
#Instructions:
# 1. Ask the user for two inputs:
#    A number (integer).
#   A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

#Example 1:
#Input:
#number: 7
#length: 5
#Output: [7, 14, 21, 28, 35]

user_num = int(input("Choose a number: "))
user_len = int(input("Choose a length: "))

user_list = []

for num in range(1,user_len + 1):
    user_list.append(user_num * num)
print(user_list)

#Challenge 2: Remove Consecutive Duplicate Letters
# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

#The new string should only contain unique consecutive letters.
#For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
#3. The program should print the modified string.

#Example 1:
# Input: user’s word: "ppoeemm"
# Output: "poem"

user_input = input("Type a word: ")

user_string = ""

for char in user_input:
    if user_string == "" or char != user_string[-1]:
        user_string += char
print(user_string)
