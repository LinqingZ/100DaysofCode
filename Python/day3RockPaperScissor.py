import random

user_choice = input("Choose 0 for rock, 1 for paper or 2 for scissors: ")
computer_choice = random.randint(0, 2)

choices = ["rock", "paper", "scissors"]

user_choice = int(user_choice)

print(f"You chose {choices[user_choice]}")
print(f"The computer chose {choices[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
# elif computer_choice > user_choice:
#         print("You lose!") # this maybe redundant 
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")

