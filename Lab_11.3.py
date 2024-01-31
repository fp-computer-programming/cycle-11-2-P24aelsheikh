"""
1. Create a Python file named lab_11-3.py
2. Create a function named number_guess that generates a random
number between 1 and 100 and asks a user to guess the number.
• If the used guessed correctly, return a congratulations message.
• If the user was incorrect, return a message stating they were not correct and
indicate if they number was higher or lower than their guess
3. The program should run until the used correctly guesses the
number.
4. The program must contain a while loop with a trigger
"""
# Author: Alsir Elsheikh
import random

def number_guess():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize a variable to control the while loop
    guessed_correctly = False
    
    # Start the game loop
    while not guessed_correctly:
        # Ask the user to input their guess
        user_guess = int(input("Guess the number between 1 and 100: "))
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            guessed_correctly = True
        else:
            # Provide a hint if the guess is incorrect
            if user_guess < secret_number:
                print("Incorrect. The number is higher.")
            else:
                print("Incorrect. The number is lower.")

# Call the function to start the game
number_guess()
