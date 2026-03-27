# Exercise 1: Converting Lists into Dictionaries
# Instructions: 
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = {}

for k,v in zip(keys,values):
    new_dict[k] = v

print(new_dict) #{'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Exercise 2: Cinemax #2
# Instructions: Write a program that calculates the total cost of movie tickets for a family based on their ages.
    #Family members’ ages are stored in a dictionary.
    #The ticket pricing rules are as follows:
        #Under 3 years old: Free
        #3 to 12 years old: $10
        #Over 12 years old: $15


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
name = input("Type name of family member: ")

if name in family:
    age = family[name]
        
    if age <= 3:
        print(f"{name} pays nothing")
    elif age <= 12:
        print(f"{name} pays $10")
    else:
        print(f"{name} pays $15")
else:
    print("Wrong name")

# Exercise 3: Zara
# Instructions: Create and manipulate a dictionary that contains information about the Zara brand.

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
    "US": ["pink", "green"]}
}

#Create a dictionary called brand with the provided data.
#Modify and access the dictionary as follows:
    #Change the value of number_stores to 2.
brand["number_stores"] = 2
    #Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara has clothes for everone. soome for {brand["type_of_clothes"][0]}, Some for {brand["type_of_clothes"][1]}, and even {brand["type_of_clothes"][2]}!")
    #Add a new key country_creation with the value Spain.
brand.update({"country_creation":"Spain"})
    #Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    band["international_competitors"].append("Desigual")
    #Delete the creation_date key.
del brand["creation_date"]
    #Print the last item in international_competitors.
print(brand[.pop(]"international_competitors"][-1])
    #Print the major colors in the US.
print(brand["major_color"]["US"])
    #Print the number of keys in the dictionary.
print(len(brand.keysx()))
    #Print all keys of the dictionary.
print(brand.key())


