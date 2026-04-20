# # Exercise 1
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# cat1 = Cat("Stinky", 5)
# cat2 = Cat("Fluffy", 7)
# cat3 = Cat("Snowy", 10)
#
# def oldest_cat(cats):
#     oldest = max(cats, key=lambda cat: cat.age)
#     return f"The oldest cat is {oldest.name}, and he is {oldest.age} years old."
#
# print(oldest_cat([cat1, cat2, cat3]))

# Exercise 2

# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def bark(self):
#         print(f"{self.name} goes woof!")
#
#     def jump(self):
#         print(f"{self.name} jumps {self.height * 2} cm high!")
#
#     @staticmethod
#     def dog_size(dogs):
#         biggest = max(dogs, key=lambda dog: dog.height)
#         print(f"{biggest.name} is the bigger dog!")
#
#
# davids_dog = Dog("David's Dog", 25)
# sarahs_dog = Dog("Sarah's Dog", 50)
#
# sarahs_dog.bark()
# davids_dog.bark()
# sarahs_dog.jump()
# davids_dog.jump()
# Dog.dog_size([davids_dog, sarahs_dog])