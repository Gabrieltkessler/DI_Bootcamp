# Exercise 1: Cats

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Stinky", 5)
cat2 = Cat("Fluffy", 7)
cat3 = Cat("Snowy", 10)

def oldest_cat(cats):
    oldest = max(cats, key=lambda cat: cat.age)
    return f"The oldest cat is {oldest.name}, and he is {oldest.age} years old."

print(oldest_cat([cat1, cat2, cat3]))

# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

    @staticmethod
    def dog_size(dogs):
        biggest = max(dogs, key=lambda dog: dog.height)
        print(f"{biggest.name} is the bigger dog!")


davids_dog = Dog("David's Dog", 25)
sarahs_dog = Dog("Sarah's Dog", 50)

sarahs_dog.bark()
davids_dog.bark()
sarahs_dog.jump()
davids_dog.jump()
Dog.dog_size([davids_dog, sarahs_dog])

# Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(f"These are the song lyrics: {self.lyrics}")

stairway = Song("There’s a lady who's sure all that glitters is gold and she’s buying a stairway to heaven")

stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        return self.animals

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        grouped = {}

        for animal in sorted(self.animals):
            letter = animal[0].upper()

            if letter not in grouped:
                grouped[letter] = []

            grouped[letter].append(animal)
        return grouped

    def get_groups(self):
        return self.sort_animals()

jerusalem_zoo = Zoo("Jerusalem Zoo")

jerusalem_zoo.add_animal("Giraffe")
jerusalem_zoo.add_animal("Bear")
jerusalem_zoo.add_animal("Baboon")

print(jerusalem_zoo.get_animals())

jerusalem_zoo.sell_animal("Bear")

print(jerusalem_zoo.get_animals())
print(jerusalem_zoo.sort_animals())
print(jerusalem_zoo.get_groups())

