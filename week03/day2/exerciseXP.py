# exercise 1

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking")

class Bengal(Cat):
    pass

class Chartreux(Cat):
    pass

class Siamese(Cat):
    pass

class Pets:
    def __init__(self, animals):
         self.animals = animals

    def walk(self):
        for animal in self.animals:
            animal.walk()


bengal_cat = Bengal("Tony", 12)
chartreux_cat = Chartreux("Sasha", 9)
siamese_cat = Siamese("Chester", 7)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()

# exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * self.weight

        if my_score > other_score:
            print(f"{self.name} won the fight against {other_dog.name}")
        else:
            print(f"{other_dog.name} won the fight against {self.name}")

dog1 = Dog("Marley", 5, 10)
dog2 = Dog("Jojo", 10, 90)
dog3 = Dog("Manny", 7, 50)
#
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))

# exercise 3

import random

class PetDog(Dog):
    def __init__(self, name, age, trained=False):
        super().__init__(name, age)  # inherit name & age
        self.trained = trained

    def train(self):
        self.bark()  # call parent method
        self.trained = True

    def play(self, *args):
        # collect all dog names (including self)
        dogs = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dogs)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        else:
            print(f"{self.name} is not trained yet.")

# exercise 4

class Person:
    def __init__(self, first_name, age, last_name):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members.append(person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

        print("Person not found")

    def family_presentation(self):
        print(self.last_name)
        for member in self.members:
            print(member.first_name, member.age)

my_family = Family("Kessler")

my_family.born("Ariel", 5)
my_family.born("Eitan", 3)

my_family.family_presentation()

my_family.check_majority("Ariel")
my_family.check_majority("Eitan")