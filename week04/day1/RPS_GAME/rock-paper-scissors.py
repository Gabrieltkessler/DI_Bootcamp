

def get_user_menu_choice():
    print("\n1. Play new game\n"
          "2. Show scored\n"
          "3. Quit")

    user_choice = input("Enter your choice (1-3): ").strip()

    if user_choice == "1":
        return "play"
    elif user_choice == "2":
        return "Scores"
    elif user_choice == "3":
        return "Thank you for playing"
    else:
        print("Invalid choice")
        return None


def print_results(results):
    print("----Game Results----\n"
          f"Wins: {results['win']}\n"
          f"Losses: {results['loss']}\n"
          f"Draws: {results['draw']}"
          f"Thanks for playing!")

from game import Game

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        user_choice = get_user_menu_choice()

        if user_choice is None:
            continue

        if user_choice == "play":
            game = Game()
            result = game.play()
            results[result] += 1

        elif user_choice == "scores":
            print_results(results)

        elif user_choice == "quit":
            print_results(results)
            break
if __name__ == "__main__":
    main()