# Module for generating random integers
import random

import hangman
import words


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

