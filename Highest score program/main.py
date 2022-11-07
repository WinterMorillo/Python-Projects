"""
    This is the highest score program!

    After executing this program, you'll be asked to enter the list of score without any commas
    only add the value, space and the following value, after you hit enter the highest value will
    be displayed.

    Steps:

    Enter the values to evaluate by adding a space to divide each of the value and hit enter.
"""

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

heightest = 0
for score in student_scores:
    if score > heightest:
        heightest = score


print(heightest)