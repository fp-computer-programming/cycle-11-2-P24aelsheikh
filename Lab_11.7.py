"""
1. Create a Python file named lab_11-7.py
2. Using the same approach as lab 1, write a program that prints all
the numbers that are multiples of 3 in a list. Be sure your program
uses a continue statement
"""
# Author: Alsir Elsheikh

# Sample list of numbers
numbers = [1, 3, 7, 9, 12, 18, 21, 25, 30]

# Iterate through the list
for num in numbers:
    # Check if the number is not a multiple of 3
    if num % 3 != 0:
        # Skip to the next iteration
        continue
    
    # Print the number if it is a multiple of 3
    print(f"{num} is a multiple of 3")
