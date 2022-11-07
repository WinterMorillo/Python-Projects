"""
This is split calculator program
You went out with your friends and it is time to pay for the bill?

Use this program to determine what the amount each of your friends need to pay

Steps:

Enter the total bill
Enter the amount of people you want to divide the bill in
Enter the percentage bill e.g.(10%, 15%, 20%)

And get the split amount each of you need to pay

"""

print("Welcome to my interactive tip calculator!")
total_bill = float(input("What was the total bill? $"))
people_amount = float(input("How many people to split the bill? "))
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")


def percentage_amount(tip, bill):
    """This function will return the total bill amount including the tip percentage"""
    if tip == "10":
        return bill * 1.10
    elif tip == "12":
        return bill * 1.12
    elif tip == "15":
        return bill * 1.15
    else:
        return "Percentage entered is not available"


Amount_be_paid = percentage_amount(percentage_tip, total_bill)
each_people_should_paid = str(round((Amount_be_paid / people_amount), 1))

print("Each person should paid $" + each_people_should_paid)
