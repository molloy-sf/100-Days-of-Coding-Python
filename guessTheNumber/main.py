# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo


def which_level():
    level_options = ["e", "h"]
    level = ""
    while level not in level_options:
        level = input("Do you want an 'e'asy or 'h'ard level (e/h): ")
        if level == "e":
            guesses = 10
            print("You have 10 chances to guess the correct number.")
        elif level == "h":
            guesses = 5
            print("You have 5 chances to guess the correct number.")
        else:
            print("Please enter 'e' or 'h' only.")
    return guesses


def lets_play():
    print(logo)
    guess_total = which_level()
    guessed_correctly = False
    number_to_guess = randint(1, 100)
    # print(number_to_guess)
    print("Guess a random number between 1 and 100\n")
    while guess_total > 0 and not guessed_correctly:
        guess = int(input("What is your guess? "))
        guess_total -= 1
        if guess > number_to_guess:
            print("\tYour guess is too high.")
            print(f"You have {guess_total} guesses remaining.")
        elif guess < number_to_guess:
            print("\tYour guess is too low.")
            print(f"You have {guess_total} guesses remaining.")
        else:
            print(f"You guessed it!! (the number was {number_to_guess})")
            guessed_correctly = True
            print(f"You had {guess_total} guesses remaining.")
    if not guessed_correctly:
        print(f"Out of guesses, game over (the number was {number_to_guess})")


want_to_play = input("Do you want to play a game of Guess the Number? (y/n): ")
if want_to_play == "y":
    lets_play()
else:
    print("Thanks. Bye.")




