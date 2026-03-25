user_name = input("Enter your name here ")

while user_name != int(user_name) and len(user_name) > 3:
    print("thank you")
else:
    print("Please try to type your name again")