import anagram_checker

checker = anagram_checker.AnagramChecker("sowpods.txt")
def acceptable_input(word):
    word = word.strip()

    if len(word.split()) > 1:
        return False, "Too many words! Please submit only one word: "

    if not word.isalpha():
        return False, "Please submit only letters."

    return True, word.lower()

while True:
    user_input = input("Please submit only one word or exit: ")

    if user_input.lower() == "exit":
        print("Goodbye")
        break

    valid, result = acceptable_input(user_input)
    if not valid:
        print(result)
        continue

    word = result

    anagrams = checker.get_anagrams(word)

    print(
        f"Your word is: {word}\n"
        f"This is a valid English word\n"
        f"Anagrams for your word are: {anagrams}"
    )


