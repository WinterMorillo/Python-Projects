"""
    Welcome to the final hangman game!

    This project was kind of hard and challenging for me, but we did it!
    The project can still be improved, and you are more than welcome to leave your feedbacks and also,
    to clone the repository and play around with the code to make it better.

    After running the code you will be asked to enter a letter to start playing around.
    If the letter entered is in the word, you will start looking at the word with the letter fill in
    the position of the final word, but in case the word entered is wrong you will start looking at the
    thi hanged man body.

    This code was first run in replit to use the clear module, so each time a new letter has been
    guessed the previous one will be deleted, so you can better look at the screen, so I would comment out the
    line of code importing the clear module so the code can run smoothly. The link to run the code in replit will
    also be included.

    Link to my replit: https://replit.com/@WinterMorillo/Day-7-Hangman-5-Start#main.py

    Steps:

    Enter a letter you think would be in the word.
        Hint: I would recommend starting with a vowel letter, since most of the word includes a vowel in it.
    Start guessing the word and good look.
"""

import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed the letter " + guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You have entered an incorrect letter, Sorry! You have {lives} left")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])