"""
1. Create a Python file named lab_11-6.py
2. Using a while loop, write a program that prompts the user to input
a number.
3. If the user inputs a number, add that to the sum of the previous
numbers entered.
4. If the user enters -1, the program should end and display the sum of
all the numbers entered.
5. Be sure the program uses a break statement
"""
# Author: Alsir Elsheikh

# Initialize sum
total_sum = 0

while True:
    # Prompt user for input
    user_input = input("Enter a number (or -1 to end): ")

    # Check if the input is a valid number
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the user wants to end the program
    if number == -1:
        break

    # Add the number to the sum
    total_sum += number

# Display the sum of all numbers entered
print(f"Sum of all numbers entered: {total_sum}")
