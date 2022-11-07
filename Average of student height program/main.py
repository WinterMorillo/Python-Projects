"""
    This is the average height student program!

    With this program you will be able to determine the average height of the student in the class.

    Steps:

    Enter the height of the student without any other character other than the number e.g. 10 20 30 40,
    and hit enter, that will return the average height of the class' student.
"""

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    height_total = 0
    for height in student_heights:
        height_total += int(height)
    contador = n + 1
    average = round(height_total / contador)
    
print(average)
