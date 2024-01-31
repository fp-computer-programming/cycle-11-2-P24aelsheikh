"""
1. Create a Python file named lab_11-4.py
2. Create a function named fibonacci. The function should take in a
user generated number from 2-100.
3. Generate & print the fibonacci sequence with the same number of
values as the user input.
4. Add the numbers in the fibonacci sequence together & return this
value.
"""
# Author: Alsir Elsheikh
def fibonacci(n):
    # Initialize the first two numbers in the sequence
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence with n values
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    # Print the Fibonacci sequence
    print(f"Fibonacci sequence with {n} values: {fib_sequence}")

    # Add the numbers in the Fibonacci sequence together
    sum_fibonacci = sum(fib_sequence)

    return sum_fibonacci

def main():
    # Ask the user to input a number between 2 and 100
    user_input = int(input("Enter a number between 2 and 100: "))

    # Validate user input
    if 2 <= user_input <= 100:
        # Call the fibonacci function with user input
        result = fibonacci(user_input)
        print(f"Sum of the Fibonacci sequence: {result}")
    else:
        print("Invalid input. Please enter a number between 2 and 100.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
