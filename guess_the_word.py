# Word Guessing Game
# This program selects a random word and allows the user
# to guess one letter at a time until the word is solved
# or the player runs out of attempts.

import random

# Predefined list of words
word_list = ["python", "computer", "programming", "developer", "keyboard"]

# Randomly select a word
secret_word = random.choice(word_list)

# Create a list of underscores to hide the word
display_word = ["_"] * len(secret_word)

# Number of incorrect guesses allowed
attempts_left = 6

# Store letters already guessed
guessed_letters = []

print("Welcome to the Word Guessing Game!")
print("Try to guess the word one letter at a time.")

# Main game loop
while attempts_left > 0 and "_" in display_word:

    # Display current progress
    print("\nWord:", " ".join(display_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Attempts Remaining:", attempts_left)

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
     
