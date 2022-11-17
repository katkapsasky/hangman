"""
Code for creating a hangman game in python
"""

# Module to enable function to clear code between functions
import os

# Modules for generating random integers
# and adding a time lag between steps
import random
import time

# Import files with words to be guessed
from easy import *
from medium import *
from hard import *

# Import file to draw the hangman
from hangman import *

global NAME
global DIFF_LEVEL
global GAME_OVER
GAME_OVER = False


def clear():
    """
    Clear function to clean-up the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


# Welcome
def get_username():
    while True:
        global NAME
        NAME = input('Welcome to Hangman! Please enter your name:\n')
        clear()
        if NAME.isalpha():
            print(f"Hi {NAME}!")
            print(
                "The aim of Hangman is to guess the secret "
                "word chosen by the computer.")
            break
        else:
            print(f"{NAME} is not valid. Please try again.")


# Choose difficulty
def choose_diff():
    """
    Function for user to choose difficulty level
    """
    prompt = "Please choose a level (easy, medium, hard).\n>"
    choice = ""
    while choice not in ['easy', 'medium', 'hard']:
        choice = input(prompt)
    return current_diff(choice)


time.sleep(1)


def current_diff(level):
    """
    Function to inform user of difficulty
    level chosen
    """
    message = "You picked " + level
    print(message)
    DIFF_LEVEL = level
    time.sleep(1)
    print("Let's play!")
    return DIFF_LEVEL


class Hangman():
    """
    Game class with methods
    """
    def __init__(self, secret_word):
        self.wrong_guess = 0
        self.secret_word = secret_word
        self.progress = list('_' * len(self.secret_word))

    def find_secret_word_letters(self, letter):
        """
        Method to take a letter and return a list
        with the secret word's indexes
        """
        return [i for i, char in enumerate(self.secret_word) if letter == char]

    def invalid_input_digit(self, input_):
        """
        Method to validate if the user input is correct
        Checks if the user inputs a number
        """
        return input_.isdigit()

    def invalid_input_len(self, input_):
        """
        Method to validate if the user input is correct
        Checks if the user inputs more than one character
        """
        return input_.isalpha() and len(input_) > 1

    def print_game_status(self):
        """
        Method to print the secret word with the letters guessed
        and remaining blank spaces
        """
        print('\n')
        print('\n'.join(HANGMAN[:self.wrong_guess]))
        print('\n')
        print(' '.join(self.progress))

    def update_progress(self, letter, indexes):
        """
        Method to update the secret word with the guessed letters
        """
        for index in indexes:
            self.progress[index] = letter

    def get_user_input(self):
        """
        Method to get the user's guess
        """
        user_input = input('\nEnter your guess here:\n')
        return user_input

    def replay(self):
        """
        Method to ask user if they want to replay
        """
        user_replay = input('\nWould you like to play again? Type Y or N:\n')
        return user_replay

    def play(self):
        """
        Method to play the game
        Asks user for a letter until they guess the word
        or they run out of guesses
        """
        while self.wrong_guess < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            # Validate user input
            if self.invalid_input_digit(user_input):
                print('Please guess a letter!')
                continue
            if self.invalid_input_len(user_input):
                print('Please guess only one letter at a time!')
                continue
            # Check if the letter has already been guessed
            if user_input in self.progress:
                print('You have already guessed that letter!')
                continue
            clear()
            # Update word with correct guess
            if user_input in self.secret_word:
                indexes = self.find_secret_word_letters(user_input)
                self.update_progress(user_input, indexes)
                # If the user guesses all letters
                # before running out of attempts they win
                if self.progress.count('_') == 0:
                    print('\nYay! You won!')
                    print(f'The word is {secret_word}')
                    time.sleep(2)
                    clear()
                    # Check if user would like to play again
                    user_prompt = self.replay()
                    if user_prompt.lower() == 'n':
                        print(f'Thanks for playing {NAME}!')
                        quit()
                        break
                    elif user_prompt.lower() == 'y':
                        break
                    else:
                        print(f"{user_prompt} is not valid.")
                        print("Please enter Y to play again or N to quit")
            else:
                self.wrong_guess += 1

            if self.wrong_guess == len(HANGMAN):
                self.print_game_status()
                print('\nOh no! You lost!')
                time.sleep(2)
                clear()
                while True:
                    user_prompt = self.replay()
                    if user_prompt.lower() == 'n':
                        print(f'Thanks for playing {NAME}!')
                        GAME_OVER = True
                        quit()
                    elif user_prompt.lower() == 'y':
                        break
                    else:
                        print(f"{user_prompt} is not valid.")
                        print("Please enter Y to play again or N to quit")


if __name__ == '__main__':
    get_username()
    while GAME_OVER is False:
        DIFF_LEVEL = choose_diff()
        if DIFF_LEVEL == 'easy':
            secret_word = random.choice(EASY_WORDS)
        elif DIFF_LEVEL == 'medium':
            secret_word = random.choice(MEDIUM_WORDS)
        else:
            secret_word = random.choice(HARD_WORDS)
        clear()
        hangman = Hangman(secret_word)
        hangman.play()
