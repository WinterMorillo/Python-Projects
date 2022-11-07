"""
    This is a pizza ordering program!
    You would be able to see the menu and based on your preferences order your pizza.

    Steps:

    Read the menu.
    See extra available options.
    Get your pizza and final bill!
"""

print("Welcome to Python Pizza\nWe have different pizzas, please select:\nSmall Pizza $15\nMedium Pizza $20\n"
      "Large Pizza $25\n\nPepperoni for small pizzas +$2\nPepperoni for Medium or Large pizzas +$3\n\n"
      "Extra cheese for any size oz pizza +$1\n")

customer_size_pizza = input("Please enter the size of your pizza\n")
order_total = 0

if customer_size_pizza == "s":
    order_total = 15
elif customer_size_pizza == "m":
    order_total = 20
elif customer_size_pizza == "l":
    order_total = 25
else:
    print(f"The order total is {order_total}")

extra_pepperoni = input("Would you like to add extra pepperoni? ")
if extra_pepperoni == "y":
    if customer_size_pizza == "s":
        order_total += 2
    else:
        order_total += 3
extra_cheese = input("Would you like to add extra cheese? ")
if extra_cheese == "y":
    order_total += 1
    print(f"The order total is {order_total}")
else:
    print(f"The order total is {order_total}")