"""
    Welcome to the title program!

    This program will convert the input from the user to title case, in simple words,
    the user enters a word that the letters can be in lower case, other in upper case,
    and after the program has been executed, word entered, the program will return the word,
    with the first letter of the word in uppercase and the rest of the letter in lower case.

    Steps:

    Enter the word and hit enter.

    This will return the word in title case.
"""

name = input("Please enter your name: ")


def format_name(name):
    """This function takes name and last name of the user,
    convert them into a title, and then it returns them"""
    print(name.title())


format_name(name)
