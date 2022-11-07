"""
    Welcome to the Higher Lower Game!

    In this game your challenge about instagram celebrities would be tested.
    You'll be given two different celebrities, and you'll have to guess which of the two of them
    has more followers than the other, each correct answer will give you a point, otherwise
    you'll lose.

    Steps:

    Based on your instagram celebrities knowledge, enter either A or B celebrity has more
    followers than the other.

    Good Luck, and enjoy the game!
"""

from game_data import data
import random
from art import logo, vs
# from replit import clear


# Creating a function to return a random Value
def get_random_account():
    return random.choice(data)


# Creating a function to return the value formatted
def formatting_account(user):
    name = (user["name"])
    description = (user["description"])
    country = (user["country"])
    return f"{name}, {description}, from {country}."


# Creating a function to verify the answer and return values
def check_guess(guess, c_followers, a_followers):
    if c_followers > a_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    game_should_continue = True
    a_user = get_random_account()
    score = 0

    while game_should_continue:
        c_user = a_user
        while c_user == a_user:
            a_user = get_random_account()

        print(f"Compare A: {formatting_account(c_user)}")
        print(vs)
        print(f"Against B: {formatting_account(a_user)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        c_followers = c_user["follower_count"]
        a_followers = a_user["follower_count"]

        # clear()
        print(logo)
        is_correct = check_guess(guess, c_followers, a_followers)
        if is_correct:
            score += 1
            print(f"You are right! Your current score is {score}.")
        else:
            print(f"Sorry, you lost! Your final score is {score}.")
            game_should_continue = False


game()





