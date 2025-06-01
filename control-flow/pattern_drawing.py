#!/usr/bin/env python3
"""
Pattern Drawing with Nested Loops
"""

try:
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Please enter a positive integer.")
    else:
        row = 0
        while row < size:
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next line after each row
            row += 1

except ValueError:
    print("Invalid input. Please enter a positive integer.")
