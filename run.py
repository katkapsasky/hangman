"""
Code for creating a hangman game in python
"""
# Import file to draw the hangman
from hangman import *

# Import files with words to be guessed
from easy import *
from medium import *
from hard import *

# Module to enable function to clear screen in game play
import os

# Modules for generating random integers
# and adding a time lag between steps
import random
import time

# Module to add color to the console
import colorama
from colorama import Fore, Back, Style
# Initiate colorama to work on windows
# and reset text color after new line
colorama.init(autoreset=True)

# Global variables
global NAME
global MENU_CHOICE
global READY_TO_PLAY
global DIFF_LEVEL
global GAME_OVER
GAME_OVER = False


def clear():
    """
    Clear function to clean-up the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_username():
    """
    Function to get and print username
    """
    while True:
        global NAME
        NAME = input("Please enter your name:\n")
        if NAME.isalpha():
            clear()
            print(f"{Fore.CYAN}Hi {NAME}!")
            break
        else:
            print(
                f"{Back.RED}{Fore.WHITE}{NAME} is not valid. \n"
                "Please try again."
            )


def main_menu():
    """
    Function for user to choose to play,
    read the game rules, or quit
    """
    print(
        f"{Fore.BLUE}Welcome to Hangman! \n"
        "The aim of the game is to guess the secret word "
        "chosen by the computer."
    )
    while True:
        global MENU_CHOICE
        MENU_CHOICE = input(
            f"{Fore.MAGENTA}Type P to Play, R for the Game Rules "
            "or Q to Quit:\n"
        )
        clear()
        if MENU_CHOICE.lower() == "p":
            print(f"{Fore.GREEN}Let's play!")
            time.sleep(2)
            clear()
            break
        elif MENU_CHOICE.lower() == "r":
            print(f"{Fore.BLUE}HANGMAN GAME RULES")
            print(
                f"{Back.BLUE}{Fore.WHITE}The aim of the game "
                "is to guess the secret "
                "word chosen by the computer.")
            print(
                f"{Back.BLUE}{Fore.WHITE}Every wrong guess will result in "
                "part of the hangman being drawn. \n"
                "If you guess incorrectly 7 times, "
                "the hangman will be fully formed and you lose."
            )
            print(
                f"{Back.BLUE}{Fore.WHITE}To win, guess the letter "
                "before you run out of attempts."
            )
            print(
                f"{Back.BLUE}{Fore.WHITE}Before you play "
                "you will have the option to choose "
                "the difficulty of the word to guess; \n"
                "easy, medium or hard"
            )
            global READY_TO_PLAY
            READY_TO_PLAY = input(
                "Are you ready to play? Type Y to play "
                "or N to quit:\n"
            )
            clear()
            if READY_TO_PLAY.lower() == "y":
                break
            elif READY_TO_PLAY.lower() == "n":
                print(f"{Fore.CYAN}See you later {NAME}!")
                quit()
            else:
                print(f"{Back.RED}{Fore.WHITE}{READY_TO_PLAY} is not valid.")
        elif MENU_CHOICE.lower() == "q":
            print(f"{Fore.CYAN}See you later {NAME}!")
            quit()
        else:
            print(f"{Back.RED}{Fore.WHITE}{MENU_CHOICE} is not valid.")


# Choose difficulty
def choose_diff():
    """
    Function for user to choose difficulty level
    """
    prompt = "Please choose a level (easy, medium, hard).\n>"
    choice = ""
    while choice.lower() not in ["easy", "medium", "hard"]:
        if choice.lower() != "":
            clear()
            print(f"{Back.RED}{Fore.WHITE}{choice} is not valid!")
        choice = input(prompt)

    return current_diff(choice)


time.sleep(1)


def current_diff(level):
    """
    Function to inform user of difficulty
    level chosen
    """
    DIFF_LEVEL = level
    print(f"You picked {level}!")
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
        self.progress = list("_" * len(self.secret_word))
        self.used_words = set()

    def find_secret_word_letters(self, letter):
        """
        Method to take a letter and return a list
        with the secret word's indexes
        """
        return [i for i, char in enumerate(self.secret_word) if letter == char]

    def invalid_input_not_alpha(self, input_):
        """
        Method to validate if the user input is correct
        Checks if the user inputs anything but an
        alphabetical character
        e.g. numbers, special characters or empty inputs
        """
        return input_.isalpha()

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
        print("\n")
        print("\n".join(HANGMAN[:self.wrong_guess]))
        print("\n")
        print(" ".join(self.progress))

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
        user_input = input(f"\n{Fore.BLUE}Enter your guess here:\n")
        return user_input.lower()

    def replay(self):
        """
        Method to ask user if they want to replay
        """
        user_replay = input("\nWould you like to play again? Type Y or N:\n")
        clear()
        return user_replay.lower()

    def play(self):
        """
        Method to play the game
        Asks user for a letter until they guess the word
        or they run out of guesses
        """
        while self.wrong_guess < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()
            # Check input is only one letter
            if self.invalid_input_len(user_input):
                print(
                    f"{Back.RED}{Fore.WHITE}Please guess only "
                    "one letter at a time!"
                )
                continue
            # Check if a letter has already been guessed
            if user_input in self.progress or user_input in self.used_words:
                print(
                    f"{Back.RED}{Fore.WHITE}You have already "
                    "guessed that letter!"
                )
                continue
            # If input is a letter remember it
            # so user is notified if they guess it again
            if self.invalid_input_not_alpha(user_input):
                self.used_words.add(user_input)
            else:
                # If guess not alphabetical letter
                print(
                    f"{Back.RED}{Fore.WHITE}Invalid guess! "
                    "Please only guess alphabetical letters!"
                )
                continue
            clear()
            # Update word with correct guess
            if user_input in self.secret_word:
                indexes = self.find_secret_word_letters(user_input)
                self.update_progress(user_input, indexes)
                # If the user guesses all letters
                # before running out of attempts they win
                if self.progress.count('_') == 0:
                    print(
                        f"\n{Fore.GREEN}Yay! You won!"
                    )
                    print(f"The word is {Fore.GREEN}{secret_word}")
                    input("Press any key to proceed\n")
                    clear()
                    # Check if user would like to play again
                    user_replay = self.replay()
                    while user_replay not in ("y", "n"):
                        print(
                            f"{Back.RED}{Fore.WHITE}{user_replay} "
                            "is not valid."
                        )
                        user_replay = self.replay()
                    if user_replay.lower() == "n":
                        print(f"{Fore.CYAN}Thanks for playing {NAME}!")
                        quit()
                    elif user_replay.lower() == "y":
                        break

            else:
                self.wrong_guess += 1

            # If user runs out of attempts they lose
            if self.wrong_guess == len(HANGMAN):
                self.print_game_status()
                print(f"\n{Fore.RED}Oh no! You lost!")
                print(f"The word is {Fore.RED}{secret_word}")
                input("Press any key to proceed")
                clear()
                while True:
                    user_prompt = self.replay()
                    clear()
                    if user_prompt.lower() == "n":
                        print(f"{Fore.CYAN}Thanks for playing {NAME}!")
                        GAME_OVER = True
                        quit()
                    elif user_prompt.lower() == "y":
                        break
                    else:
                        print(
                            f"{Back.RED}{Fore.WHITE}{user_prompt} "
                            "is not valid."
                        )


if __name__ == "__main__":
    get_username()
    main_menu()
    while GAME_OVER is False:
        DIFF_LEVEL = choose_diff()
        if DIFF_LEVEL.lower() == "easy":
            secret_word = random.choice(EASY_WORDS)
        elif DIFF_LEVEL.lower() == "medium":
            secret_word = random.choice(MEDIUM_WORDS)
        else:
            secret_word = random.choice(HARD_WORDS)
        clear()
        hangman = Hangman(secret_word)
        hangman.play()
