"""
Task #1
Explain the difference between the = operator and the == operator in Python.
Answer
= (Assignment Operator):
The = operator is used for variable assignment. It assigns a value to a variable.
When you use the = operator, you are telling Python to store a specific value in a variable.
for example: x = 5

== (Equality Operator):
The == operator is used to check for equality between two values or expressions.
It returns True if the values on the left and right side are equal and False if they are not.
The == operator is used in conditional statements and comparisons.
For example:
x = 5
y = 5
result = (x == y)

What does the ** operator do in Python, and how is it used?
Answer:
it is basically E to power. 

In Python, the ** operator is used for exponentiation.
It raises a number to a specific power. It is also known as the "power" or "exponentiation" operator.
The ** operator works with both integers and floating-point numbers.

a= 2**3 # result will be 8

What does the ^ operator do in Python, and in what context is it commonly used?
"""
# Task 2
# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

r = int(input("Enter the radius\n"))
pi = float(3.14)

area = pi * r ** 2
print('The area of the circle is', area)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.
"""
a=int(input("Enter the number\n"))
b=int(input("Enter the number\n"))

result= if a ==b
"""

# Use the ternary operator to find the maximum of three numbers entered by the user.
First_num = int(input("Enter the first number\n"))
Second_num = int(input("Enter the second number\n"))
Third_num = int(input("Enter the third number\n"))

max_value = First_num if First_num > Second_num else Second_num if Second_num > Third_num else Third_num
print("The max value between three is", max_value)

# Develop a Python script that calculates the square and cube of a given number.
#for Square of number
Sq=int(input("Enter a number\n"))
Square =Sq**2
print("The square of the Number is", Square )

#For cube of a number
Cu=int(input("Enter a number\n"))
Cube=Cu**3
print("The Cube of the Number is", Cube )