# Testing

Click to return back to the [README.md](README.md) file.

## Manual Testing

I have manually tested this project in my local terminal on GitPod and in the Code Institute Heroku terminal.

### Defensive Programming

I have tried to ensure that any invalid input while using the app and within gameplay is not accepted and an error message is shown to the user when their input is invalid:

  - Users cannot input numbers or special characters instead of letters throughout the game, whilst: 
    - Giving their name
    ![Name input validation](documentation/testing/name_validation.png)
    - Navigating the game menu options
    ![Game menu options input validation](documentation/testing/game_options_validation.png)
    - Playing the game - users cannot input numbers or special characters, guess more than one letter at once or guess a letter they have already guessed)
    ![In-game wrong input: digit](documentation/features/input_validation_digit.png)
    ![In-game wrong input: multiple letters](documentation/features/input_validation_multiple_char.png)
    ![In-game wrong input: guessing a correct letter that has already been guessed](documentation/testing/input_validation_duplicate_correct_guess.png)
    ![In-game wrong input: guessing a wrong letter that has already been guessed](documentation/testing/input_validation_duplicate_wrong_guess.png)

    - Playing again
    ![Replay option input validation](documentation/testing/invalid_replay_input.png)

---

## Validator Testing

I have passed all my code from the below files through a PEP8 linter and confirmed there are no problems.

- run.py
- easy.py
- medium.py
- hard.py
- hangman.py

---

## Bugs

### Fixed Bugs

The input validation when a user guesses a letter they have already guessed was only working when they guessed a correct letter more than once - if the letter was incorrect the user could keep guessing and would run out of attempts. 

To fix this, I created an empty set to store user guesses,
``` self.used_words = set() ``` 
and then I added an if statement to check for guessed incorrect letters and an else statement to add and remember incorrect letters so the user will receive a message they have already guessed a letter whether it was correct or incorrect and an additional part of the hangman isn't drawn. 

``` # Check if a correct letter has already been guessed
            if user_input in self.progress:
                print(f"{Back.RED}You have already guessed that letter!")
                continue
            # Check if an incorrect letter has already been guessed
            if user_input in self.used_words:
                print(f"{Back.RED}You have already guessed that letter!")
                continue
            else:
                # Remember letters guessed by user
                self.used_words.add(user_input) 
```

Another bug I found was in text formatting. Some of the text printed to the console, such as the game rules, was throwing errors as the lines were too long and the text on the console was breaking so a new line would cut a word in half, making it hard for users to read. 

By formatting my text over multiple lines and adding in new lines I was able to make the text easier to read and fix the errors.

``` print(
                f"{Back.BLUE}Every wrong guess will result in "
                "part of the hangman being drawn. \n"
                "If you guess incorrectly 7 times, "
                " the hangman will be fully formed and you lose."
            )
```

### Unfixed Bugs

There are no unfixed bugs that I am aware of.

---

