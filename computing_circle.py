# question 1
"""
Q1, Write a program which accepts the radius oof the circle from the user and computes the area

Example input:
r = 1.1

example output:
Area = 3.8

To ask for users to input, use the following:
・input(prompt)
This function first takes the input from the user and then evaluates the expression, which means Python automatically
identifies whether user entered a string or a number or list. If the input provided is not correct then either syntax error or exception is raised by python.

・raw_input(prompt)
This function works in older version (like Python 2.x). This function takes exactly what is typed from the keyboard,
convert it to string and then return it to the variable in which we want to store. For example –
Reference: (https://www.geeksforgeeks.org/taking-input-in-python/)

Step

how to interpret int nnd string
init()
str()

"""
"""My answer

r = input('Please enter the radius:')
Area = int(r) * int(r) * 3.14
print(str(Area))
"""
from math import pi

radius = input('Enter a radius:')

A = pi * (int(radius) ** 2)

print(A)
