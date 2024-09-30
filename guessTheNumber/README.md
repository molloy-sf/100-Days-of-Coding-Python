# Number Guessing Game

Welcome to the Number Guessing Game! This is a fun interactive game where players attempt to guess a randomly generated number between 1 and 100. The game provides feedback on the player's guesses and tracks the number of attempts remaining.

## Objectives

- Include an ASCII art logo.
- Allow the player to submit a guess for a number between 1 and 100.
- Provide feedback for guesses that are too high or too low.
- Reveal the correct answer if the player guesses correctly.
- Track the number of turns remaining.
- Inform the player if they run out of turns.
- Offer two difficulty levels:
  - Easy: 10 guesses
  - Hard: 5 guesses

## Requirements

- Python 3.x
- The `art` library for ASCII art (install using `pip install art`)

## Installation

1. Clone this repository or download the code files.
2. Ensure you have the necessary files:
   - `number_guessing_game.py` (the main game script)
   - `art.py` (or your ASCII art logo file)

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the game script.
3. Run the script:

   ```bash
   python number_guessing_game.py

    Follow the prompts to play the game.

How to Play

    You will be prompted to choose a difficulty level:
        Enter 'e' for Easy mode (10 guesses)
        Enter 'h' for Hard mode (5 guesses)
    Guess a number between 1 and 100.
    The game will inform you if your guess is too high or too low.
    If you guess the correct number, you win! If you run out of guesses, the game will reveal the correct number.

Example Interaction

Do you want to play a game of Guess the Number? (y/n): y
     ___
    / _ \
   | | | |
   | |_| |
    \___/
You have 10 chances to guess the correct number.
Guess a random number between 1 and 100

What is your guess? 50
    Your guess is too high.
    You have 9 guesses remaining.

What is your guess? 25
    Your guess is too low.
    You have 8 guesses remaining.

What is your guess? 37
    You guessed it!! (the number was 37)
    You had 7 guesses remaining.

Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.
License

This project is open-source and available under the MIT License.
