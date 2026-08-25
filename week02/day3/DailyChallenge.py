import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

for num in list_of_numbers:
    if num + num == target_number:
        print(f"{num} + {num} equals {target_number}")
        break