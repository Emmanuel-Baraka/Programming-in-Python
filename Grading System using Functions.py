#EMMANUEL BARAKA
#REG NO: BSCIT-05-0113/2024

#GRADING SYSTEM

marks = float(input("Enter your total marks:  "))

def calculate_grade(marks):
    if marks <0 or marks >100:
        return "Invaid marks (Must be 0 - 100)"
    if marks >= 70 and marks <=100:
        return "A"

    elif marks >= 60 and marks < 69:
        return "B"

    elif marks >=50 and marks <59:
        return "C"

    elif marks >=40 and marks < 49:
        return "D"

    else:
        return "F"

#printed using f-strings
print(f"Your grade is: {calculate_grade(marks)}")
