"""
    Welcome to the Days in the month program!

    This program is a continuation of the leap year project, we have use the same functionalities of
    that project, and implement them in this program to have into consideration when it is a leap year,
    since in a leap year February will have 29 days instead of 28.

    Steps:

    Enter the year.
    Enter the month.

    This will tell you exactly how many days there are in the month you entered.
"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = is_leap(year)
    month_has = 0
    for i in range(len(month_days)):
        month_has = month_days[month - 1]
    if year == True and month_has == 28:
        month_has += 1
    return month_has


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












