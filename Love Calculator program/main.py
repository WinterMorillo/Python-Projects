"""
    Welcome to the love calculator program!
    Main idea of the project:

    We will take the words: "True Love", we will request the couple names, and will run the program
    to determine how many times the letters of the words "True Love" are repeated on the couple names,
    then we'll add up this amount and determine the percentages of love between the couples.

    Steps:

    Just enter the name of the couple and get the love percentage.
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

full_names = (name1 + name2).lower()

t = full_names.count("t")
r = full_names.count("r")
u = full_names.count("u")
e = full_names.count("e")

l = full_names.count("l")
o = full_names.count("o")
v = full_names.count("v")
e = full_names.count("e")

love_percentage = int(str(t + r + u + e) + str(l + o + v + e))

if love_percentage < 10 or love_percentage > 90:
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")
elif love_percentage >= 40 and love_percentage <= 50:
    print(f"Your score is {love_percentage}, you are alright together.")
else:
    print(f"Your score is {love_percentage}")
