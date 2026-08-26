import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

seen = set()
found_pairs = set()

for num in list_of_numbers:
    complement = target_number - num

    if complement in seen:
        pair = tuple(sorted((num, complement)))
        found_pairs.add(pair)

    seen.add(num)

for first, second in sorted(found_pairs):
    print(f"{first} + {second} equals {target_number}")