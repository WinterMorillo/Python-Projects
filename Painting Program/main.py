"""
    Welcome to the painting calculator program!
    Let's say you need to paint a wall, but you don't know how many cans on paint you need to buy,
    so how can you start? I have the solution for you here!

    The instructions of the paint tells you that: "1 can of paint can cover 5 square meters of wall".
    Well this program will tell you based on the width and height of the wall how many cans will be needed.

    Steps:

    Enter the height of the wall.
    Enter the width of the wall.
    Hit the enter button.

    This will tell you exactly the amount cans needed to complete the job!
"""

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height=test_h, width=test_w, cover=coverage):
    nums_of_cans_needed = math.ceil((height * width) / cover)
    print(f"You'll need {nums_of_cans_needed} cans to paint the wall.")


paint_calc(height=test_h, width=test_w, cover=coverage)
