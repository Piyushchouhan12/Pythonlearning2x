"""
Task #1
✅ Grade Calculator:
Write a program that calculates and
displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
input- score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
If, elif, else
"""

Marks = float(input("Enter the marks\t"))

if Marks in range(90, 101):
    print("Your grade is A ")
elif Marks in range(80, 90):
    print("Your grade is b")
elif Marks in range(70, 80):
    print("Your grade is c")
elif Marks in range(60, 70):
    print("Your grade is D")
else:
    print("Your grade is F")

"""
Task #2
✅ Leap Year Checker:
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year
"""
Year = int(input("Enter the year\t"))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")

"""
Task #3
✅ Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, 
determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), 
or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3
"""
s1 = int(input("Enter the s1\t"))
s2 = int(input("Enter the s2\t"))
s3 = int(input("Enter the s3\t"))

if (s1 == s2 == s3):
    print("The triangle is equilateral")
elif (s1 == s2 ) or (s2== s3) or (s1==s3):
    print("The triangle is isosceles")
elif (s1 != s2 != s3) :
    print("The triangle is scalene")
else:
    print(None)
