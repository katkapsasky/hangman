"""
Code for creating a hangman game in python
"""
# Module for generating random integers
import random

# Code to create hangman
HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    r'|      /|\ ',
    '|       |',
    r'|      / \ '
]

# Words to be guessed
WORDS = [
    'hello', 'world'
]


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

    def invalid_input(self, input_):
        """
        Method to validate if the user input is correct
        Checks if the user inputs a number or more than one character
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

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
        user_input = input('\nEnter your guess here: ')
    
        return user_input

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
            if self.invalid_input(user_input):
                print('Please guess a letter!')
                continue
            # Check if the letter has already been guessed
            if user_input in self.progress:
                print('You have already guessed that letter!')
                continue

            if user_input in self.secret_word:
                indexes = self.find_secret_word_letters(user_input)
                self.update_progress(user_input, indexes)
                # If the user guesses all letters
                # before running out of attempts
                if self.progress.count('_') == 0:
                    print('\nYay! You won!')
                    print(f'The word is {0}'.format(self.secret_word))
                    quit()
            else:
                self.wrong_guess += 1
        print('\nOh no! You lost!')


if __name__ == '__main__':
    secret_word = random.choice(WORDS)
    hangman = Hangman(secret_word)
    hangman.play()
