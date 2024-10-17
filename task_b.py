grade = input("Enter a grade between 0-100: " )
if isinstance(grade, int) != True:
    print("Error: Please enter a number")
    exit()


if grade <= 100 and grade >= 80:
    letter = 'A'
elif grade < 80 and grade >= 60:
    letter = 'B'
elif grade < 60 and grade >= 50:
    letter = 'C' 
elif grade < 50 and grade >= 40:
    letter = 'D'
elif grade < 40 and grade >= 0:
    letter = 'F'
else:
    print("Error: Grades must be between 0 and 100")
    exit()

print(f"Your grade is: {letter}")

    