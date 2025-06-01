#!/usr/bin/env python3
"""
Multiplication Table Generator using a for loop
"""

try:
    number = int(input("Enter a number to see its multiplication table: "))

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
