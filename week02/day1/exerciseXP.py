# Exercise 1: What Are You Learning?
def display_message():
    print("I am learning about functions in Python.")
display_message()

# Exercise 2: What’s Your Favorite Book?
def favorite_book(title):
    print(f"One of my favorite books is {title}")
print(favorite_book("The Bat by Jo Nesbo"))

# Exercise 3: Some Geography
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")
print(describe_city("Monroe", "New York"))

# Exercise 4: Random
import random as rd
def random_num(num):
    number = rd.randint(0,100)
    if num == number:
        print("Great job. You guessed right!")
    else:
        print(f"Sorry you guessed {num} and the correct number was {number}.")
random_num(10)

# Exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size="large", text="I love Python!"):
    print(f"The shirt size is {size} and it says {text}")
print(make_shirt())
print(make_shirt("medium"))
print(make_shirt("small","This shirt is awesome!"))

# Exercise 6: Magicians…
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for name in magician_names:
        print(name)
show_magicians(magician_names)

def make_great(magician_names):
    for names in magician_names:
       print("the Great " + names)
print(make_great(magician_names))

# Exercise 7: Temperature Advice
import random as rd
def get_random_temp():
    return rd.randint(-10, 40)

def main(temp):
    get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temp > 0 and temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temp > 16 and temp < 23:
        print("Nice weather.")
    elif temp > 24 and temp < 32:
        print("A bit warm, stay hydrated.")
    elif temp > 32 and temp < 40:
        print("It’s really hot! Stay cool.")
print(main(get_random_temp()))
