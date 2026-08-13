# Exercise 1: Converting Lists into Dictionaries
# Instructions:
# You are given two lists. Convert them into a dictionary where the first list
# contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))

print(new_dict)  # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Exercise 2: Cinemax #2
# Instructions: Write a program that calculates the total cost of movie tickets
# for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0

for name, age in family.items():

    if age < 3:
        print(f"{name} pays nothing")
        total_cost += 0

    elif age <= 12:
        print(f"{name} pays $10")
        total_cost += 10

    else:
        print(f"{name} pays $15")
        total_cost += 15

print(f"The total cost for the family is ${total_cost}")


# Exercise 3: Zara
# Instructions: Create and manipulate a dictionary that contains information
# about the Zara brand.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Create a dictionary called brand with the provided data.

# Modify and access the dictionary as follows:

# Change the value of number_stores to 2.
brand["number_stores"] = 2

# Print a sentence describing Zara’s clients using the type_of_clothes key.
print(
    f"Zara has clothes for everyone. "
    f"Some for {brand['type_of_clothes'][0]}, "
    f"some for {brand['type_of_clothes'][1]}, "
    f"and even {brand['type_of_clothes'][2]}!"
)

# Add a new key country_creation with the value Spain.
brand.update({"country_creation": "Spain"})

# Check if international_competitors exists and, if so,
# add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete the creation_date key.
del brand["creation_date"]

# Print the last item in international_competitors.
print(brand["international_competitors"][-1])

# Print the major colors in the US.
print(brand["major_color"]["US"])

# Print the number of keys in the dictionary.
print(len(brand))

# Print all keys of the dictionary.
print(brand.keys())


# Exercise 4: Disney Characters
# Instructions: You are given a list of Disney characters.
# Create three dictionaries based on different patterns as shown below.

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


# 1. Create a dictionary that maps characters to their indices.

char_to_index = {}

for i, user in enumerate(users):
    char_to_index[user] = i

print(char_to_index)


# 2. Create a dictionary that maps indices to characters.

index_to_char = {}

for i, user in enumerate(users):
    index_to_char[i] = user

print(index_to_char)


# 3. Create a dictionary where characters are sorted alphabetically
# and mapped to their indices.

sorted_users = sorted(users)

sorted_char_to_index = {}

for i, user in enumerate(sorted_users):
    sorted_char_to_index[user] = i

print(sorted_char_to_index)
