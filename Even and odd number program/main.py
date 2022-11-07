"""
    Welcome to the even and odd number!

    Using this program you will be able to enter a number, and determine
    whether is an odd or even number.

    Steps:

    Enter a number and hit enter.

    The program will tell you whether it is an odd or even number.
"""

number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
