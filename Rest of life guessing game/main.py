"""
    Welcome to the rest of your life guessing game!
    This is basic program created to determine the time left if you were
    to live until you reach 90 years old, the program would give you, the days,
    weeks and months left.

    Steps:

    Just enter your actual age and that's it!
"""

# Requesting year from the user
print("Welcome to the rest of life guessing game\nThe purpose of the game is to determine how many years you have "
      "left before reaching the 90 years old\n")

age = int(input("What's your age?\n"))
years_goal = 90 - age
age_day_left = years_goal * 365
age_weeks_left = years_goal * 52
age_months_left = years_goal * 12

print(f"You have left {age_day_left} days, {age_weeks_left} weeks, {age_months_left} months left, to reach 90 years old")