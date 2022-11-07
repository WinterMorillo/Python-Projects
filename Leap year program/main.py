"""
    This is a leap year program!
    First! What is a leap year?
    A year, occurring once every four years, which has 366 days including 29 February as an intercalary day.

    In this program you will just need to enter the year, and it will tell you
    whether it is a leap year or not.

    Steps:

    Enter the year and that's it!
"""

print("Welcome to the Leap Year detector")
year = int(input("Please enter a year: \n"))

"""if year % 100 == 0 and year % 400 == 0:
  print("This is a Leap Year. Congratulations!!!")
elif year % 4 == 0 and year % 100 != 0:
  print("This is a Leap Year. Congratulations!!!")
else:
  print("This is not a Leap Year. Sorry!")"""

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")
