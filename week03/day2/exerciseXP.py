#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         print(f"{self.name} is walking")
#
# class Bengal(Cat):
#     pass
#
# class Chartreux(Cat):
#     pass
#
# class Siamese(Cat):
#     pass
#
# class Pets:
#     def __init__(self, animals):
#          self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             animal.walk()
#
#
# bengal_cat = Bengal("Tony", 12)
# chartreux_cat = Chartreux("Sasha", 9)
# siamese_cat = Siamese("Chester", 7)
#
# all_cats = [bengal_cat, chartreux_cat, siamese_cat]
#
# sara_pets = Pets(all_cats)
# sara_pets.walk()

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

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))