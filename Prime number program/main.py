"""
    Welcome to the prime program!

    This program will tell you whether the number entered is a prime number or not.

    Steps:

    Enter the number you want to check on.
    Hit the enter button.

    The program will tell you exactly whether it is a prime number ir not.
"""

n = int(input("Check this number: "))


def prime_checker(number):
    if number == 2:
        print("This is a prime number")
    elif number % 2 != 1:
        print("This is not a prime number")
    elif number / number == 1 and number / 1 == number:
        print("This is a prime number")
    else:
        print("This is not a prime number")


prime_checker(number=n)
