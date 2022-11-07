"""
    Hello, welcome to the Fizz, Buzz, FizzBuzz program!

    The logic behind this program is very simple, using the conditionals if and else if
    we will look for number divisible by 3, 5 and 3 and 5 at the same time.

    It will do the following:

    If number is divisible by 3 and 5, it'll print FizzBuzz
    if number is divisible by 3, it'll print Fizz
    If number is divisible by 5, it'll print Buzz

    Steps:

    Just run the program and by using a for loop it would loop through 100 numbers
    Printing the text above
"""

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)