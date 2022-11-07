"""
    This is the roller coaster program!
    Here you will be able to enter your height in centimeters(CM),
    and based on this information it will tell you whether you'll be able to ride it.

    Steps:

    Enter your height and get the ticket price!
"""

print("Welcome to the Python Roller Coaster")

height = int(input("Please enter your height in (CM)\n"))
age = int(input("Please enter your age\n"))
bill = 0

if height >= 120:
    print("You can ride de roller coaster")
    if age < 12:
        bill += 10
    elif age >= 12 and age < 18:
        bill += 15
    elif age >= 18 and age < 40:
        bill += 25
    else:
        print("Your ticket is on the house. Enjoy it!")

    want_picture = input("Do you want to take a picture?\n")
    if want_picture == "y":
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you can not ride the roller coaster until you grow large enough")
