#Write a Python program that allows the user to play Rock, Paper, Scissors against the computer, displaying ASCII art for each choice and determining the winner.

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(
    input(
        "Enter your choice? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors:-\n"
    )
)

if user_choice not in [0, 1, 2]:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:-")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")
