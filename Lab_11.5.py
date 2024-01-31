"""
1. Create a Python file named lab_11-5.py
2. Create a function labeled name_multiplication. Create a list of 5
names generated from user input.
3. Have the function print each name in the list the same number of
times as letters in the name.
• i.e. “John” has 4 letters and would be printed 4 times
4. Solve this using nested loops.
• BONUS: Use BOTH a for loop AND a while loop
• BONUS 2: Have the number of times a name is printed correspond to unique
the unique letters in each name instead of total letter. (i.e. “Otto” would only
be printed twice, “John” still 4 times)
"""
# Author: Alsir Elsheikh
def name_multiplication():
    # Step 2: Create a list of 5 names generated from user input
    names = [input("Enter a name: ") for _ in range(5)]

    # Step 3: Print each name in the list the same number of times as letters in the name
    for name in names:
        print(f'Original name: {name}')
        # BONUS 2: Use a set to get unique letters in the name
        unique_letters = set(name)
        
        # BONUS 2: Print each name based on unique letters
        for letter in unique_letters:
            count = name.count(letter)
            print(f'{name} has {count} occurrences of letter "{letter}"')
            # BONUS: Use both for loop and while loop
            # Using for loop
            for _ in range(count):
                print(name)
            # Using while loop
            i = 0
            while i < count:
                print(name)
                i += 1

# Call the function to execute the program
name_multiplication()
