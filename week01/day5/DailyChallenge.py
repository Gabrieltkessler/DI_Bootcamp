#Challenge 1: Letter Index Dictionary
#Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).

#    * If it is, append the current index to the list associated with that key.
#    * If it is not, create a new key-value pair in the dictionary.


user_string = input("Type a word: ")
char_str_index = {}

for i, char in enumerate(user_string):
    if char in char_str_index:
       char_str_index[char].append(i)
    else:
        char_str_index[char] = [i]

print(char_str_index)

# Challenge 2: Affordable Items
#Goal: Create a program that prints a list of items that can be purchased with a given amount of money.

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

wallet = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    # clean price
    clean_price = int(price.replace("$", "").replace(",", ""))

    # check if affordable
    if clean_price <= wallet:
        basket.append(item)
        wallet -= clean_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))