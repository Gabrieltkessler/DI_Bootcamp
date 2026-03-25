#Exercise 1: Favorite Numbers
# Instructions:
# Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers = {3,11,16,21,22,33,58,98}
# Add two new numbers to the set.
my_fav_numbers.add(100)
my_fav_numbers.add(121)
# Remove the last number you added to the set.
my_fav_numbers.remove(121)
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = {201,202,203,204,205}
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.
print(our_fav_numbers)

#Exercise 2: Tuple
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
numbers = (1,2,3,4,5)
numbers.add(6)
print(numbers)

# Exercise 3: List Manipulation
#Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
basket.remove("Banana")
# Remove "Blueberries" from the list.
basket.remove("Blueberries")
# Add "Kiwi" to the end of the list.
basket.append("kiwi")
# Add "Apples" to the beginning of the list.
basket.insert(0,"Apples")
# Count how many times "Apples" appear in the list.
#print(basket.count("Apples"))
# Empty the list.
basket.clear()
# Print the final state of the list.
print(basket) #[]

#Exercise 4: Floats
#Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers: 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
numbers = []
num = 1.5

while num <= 5:
    numbers.append(num)
    num += .5

print(numbers)

#Exercise 5: For Loop
#Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
num_range = range(1,21)
for num in num_range:
    print(num)
# Write another for loop that prints every number from 1 to 20 where the index is even.
for num in range(1,21):
    if num % 2 == 0:
        print(num)

#Exercise 6: While Loop
#Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

user_name = input("Enter your name here ")

while user_name:
    if user_name.isalpha and len(user_name) > 3:
        print("thank you")
        break
    else:
        print("Please try to type your name again")
        break

#Exercise 7: Favorite Fruits
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print: "You chose a new fruit. I hope you enjoy it!"

user_fav_fruit = input("Type your favorite fruit ")

fruit_list = []
fruit_list.append(user_fav_fruit)

fruit = input("name any fruit ")

if fruit in fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8: Pizza Toppings
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print: "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings_list = []

while True:
    toppings = input("Type some pizza toppings ")
    
    if toppings.lower() == "quit":
        break
            
    toppings_list.append(toppings)
    print(f"Adding {toppings_list} to your pizza.")
        
total = len(toppings_list) * 2.50 + 10
print(f"You've choosen {toppings_list} and your total is ${total}")

#Exercise 9: Cinemax Tickets
# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
    #Free for people under 3.
    #$10 for people aged 3 to 12.
    #$15 for anyone over 12.
#Print the total ticket cost.

age = int(input("What is your age?: "))

if age < 3:
    print("Free for you")
elif age <= 12:
    print("$10 for you")
else:
    print("$15 for you")

#Bonus:
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
    #Ask for each person’s age.
    #Remove anyone who isn’t allowed to watch.
    #Print the final list of attendees.

age = int(input("What is your age?: "))
attendees = []

if age in range(16,22):
    attendees.append(age)
else:
    print("Not invited")

print(attendees)