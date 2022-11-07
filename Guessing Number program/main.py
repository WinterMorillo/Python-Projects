"""
    Welcome to the Guessing Number Game!

    In this program you will find an interesting and challenging game, which consist
    of a random number which has been select within a range of 1-100 numbers, there are
    two modes "Easy and Hard" mode, being Hard mode the most challenging limiting the
    attempts of the user to guess the number.

    Steps:

    Enter a number and hit enter to start guessing the game,
    but be careful with the amount of attempts left based on the mode
    you selected.

    This code was first run in replit to use the clear module, so I would comment out the
    line of code importing the clear module so the code can run smoothly. The link to run the code in replit will
    also be included.

    Link to my replit: https://replit.com/@WinterMorillo/guess-the-number-start#main.py
"""

import random
# from replit import clear
import art

numbers = []

for i in range(1, 101):
    numbers.append(i)


def guess_game(attempts):
    end_game = False
    number_to_guess = random.choice(numbers)
    while not end_game:
        answer = int(input("Make a guess: "))
        if answer > number_to_guess:
            print("Too high")
            attempts -= 1
            if attempts < 1:
                print("Sorry you ran over attempts")
                end_game = True
            else:
                print(f"You have left {attempts} attempts")
        elif answer == number_to_guess:
            print("You win! Congratulations you rock!")
            end_game = True
        else:
            print("Too low")
            attempts -= 1
            if attempts < 1:
                print("Sorry you ran over attempts")
                end_game = True
            else:
                print(f"You have left {attempts} attempts")

    if input("Do you want to play again? Type 'y' to play again, 'n' to finish") == "y":
        # clear()
        game_intro()
    else:
        print("Thank you for playing, see you soon")


def game_intro():
    print(art.logo)
    decision = input(
        "Welcome to the guess number game\nWe have randomly selected a number between 1 and 100\nType the difficulty "
        "level you want to play at\n\"Easy\" or \"Hard\"\n").lower()

    easy_attempts = 10
    hard_attempts = 5

    if decision == "easy":
        guess_game(attempts=10)
    elif decision == "hard":
        guess_game(attempts=5)
    else:
        print("The option you entered is not valid, try again")


game_intro()


















