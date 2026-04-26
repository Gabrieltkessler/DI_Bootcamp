# exercise 1
import random as rd

def get_words_from_file(filename):
    with open(filename, "r") as f:
        content = f.read()

    words = content.split()
    return words

words = get_words_from_file("words.txt")
# print(words)


def get_random_sentence(sentence_length):
    words = get_words_from_file("words.txt")

    sentence_words = []

    rd.choice(words)

    for _ in range(sentence_length):
        word = rd.choice(words)
        sentence_words.append(word)

    sentence = "".join(sentence_words)

    return sentence.lower()

print(get_random_sentence(4))

def main():
    print("This program generates a random sentence")

    input_sentence = int(input("Enter sentence length between 2 and 20: "))

    if input_sentence in range(2, 21):
        sentence = get_random_sentence(input_sentence)
        print(f"You've chosen a length of {input_sentence} words: {sentence}")
    else:
        print("Please enter a number between 2 and 20")
        raise ValueError("Invalid input range")

main()

# exercise 2

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

# print(data)
# print(type(data))

salary = data["company"]["employee"]["payable"]["salary"]
print(salary)

data["company"]["employee"]["birth_date"] = "1993-11-19"
print(data["company"]["employee"])

import json

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)