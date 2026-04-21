
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
