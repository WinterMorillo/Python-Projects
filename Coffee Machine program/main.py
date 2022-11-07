"""
    Welcome to the coffee machine program!

    Running this program you'll be able to order a coffee based on your preferences and desires,
    also enter your coins, get your chance, and get a report to see the amount of resources left,
    including the amount of money the machine has after selling.

    Steps:

    Enter the type of coffee you like.
    Enter the amount of coins.
    Get your chance
    Enjoy your coffee.
"""

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffee_Maker = CoffeeMaker()
menu = Menu()
Money_Machine = MoneyMachine()

is_on = True

while is_on:
    option = input(f"What would you like to order?({menu.get_items()}): ").lower()

    if option == "report":
        Coffee_Maker.report()
        Money_Machine.report()
    elif option == "off":
        is_on = False
    else:
        drink = menu.find_drink(option)
        if Coffee_Maker.is_resource_sufficient(drink):
            if Money_Machine.make_payment(drink.cost):
                Coffee_Maker.make_coffee(drink)



