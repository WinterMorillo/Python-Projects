"""
    Welcome to the password generator program!
    After running this code you will be able to generate a random and very secured password
    to use in your websites. You'll be able to enter the amount of letters, symbols and number
    you'd like your password to have.

    Steps:

    Enter the amount of letters.
    Enter the amount of symbols.
    Enter the amount of numbers.
    Your password would be generated, you just need to copy and paste it, whenever you'd like to use it.
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

needed = []
contador = 0
for number_letter in range(1, nr_letters + 1):
    needed.append(random.choice(letters))

for nr_number in range(1, nr_numbers + 1):
    needed.append(random.choice(numbers))

for nr_symbol in range(1, nr_symbols + 1):
    needed.append(random.choice(symbols))

new_password = random.shuffle(needed)
new_password = ""
for n in range(len(needed)):
    new_password += needed[n]

print(f"Your new generated password is {new_password}")
