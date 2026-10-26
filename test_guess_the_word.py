# test_word_game.py
# These tests verify that the word-guessing game functions
# work correctly. Pytest will automatically discover and run
# any function beginning with "test_".

import pytest
from word_game import select_word, process_guess


# Test that the selected word always comes from the predefined list.
def test_select_word_from_list():

    # Create a sample word list.
    words = ["python", "computer", "keyboard"]

    # Call the function that selects a random word.
    selected_word = select_word(words)

    # Verify the chosen word exists in the original list.
    assert selected_word in words


# Test a correct guess.
def test_correct_guess():

    # Secret word used for testing.
    secret_word = "python"

    # Current display before
