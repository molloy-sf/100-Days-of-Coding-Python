rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

import random

hands = [rock, paper, scissors]
hands_name = ("Rock", "Paper", "Scissors")
user = int(input("Which do you choose? (0 for Rock, 1 for Paper, 2 for Scissors) "))
comp = random.randint(0, 2)

if user >= 3 or user < 0:
    print("You have never played Rock, Paper, Scissors before??")
else:
    print(f"You have chosen: {hands[user]}")
    print(f"The computer has chosen: {hands[comp]}")

    if user == comp:
        print("The game is a tie!")

    ## If User wins:
    elif user == 0 and comp == 2:
        print("Rock beats scissors, you win!")
    elif user == 1 and comp == 0:
        print("Paper beats rock, you win!")
    elif user == 2 and comp == 1:
        print("Scissors beats paper, you win!")

    ## If Comp wins:
    elif comp == 0 and user == 2:
        print("Rock beats scissors, Comp wins!")
    elif comp == 1 and user == 0:
        print("Paper beats rock, Comp wins!")
    elif comp == 2 and user == 1:
        print("Scissors beats paper, Comp wins!")

