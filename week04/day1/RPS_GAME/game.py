import random as rnd

class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        while True:
            user_choice = input("Rock, Paper or Scissors?: ").lower()

            if user_choice not in ["rock", "paper", "scissors"]:
                print("You chose an invalid option. Please try again: ")
            else:
                return user_choice


    def get_computer_item(self):
            return rnd.choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, user_item, computer_item):

        if user_item == computer_item:
            return "draw"
        elif user_item == "rock" and computer_item == "scissors":
            return "win"
        elif user_item == "scissors" and computer_item == "paper":
            return "win"
        elif user_item == "paper" and computer_item == "rock":
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(
            f"\nYou selected {user_item}\n"
            f"Computer selected {computer_item}\n"
            f"\nyou {result}!"
        )

        return result