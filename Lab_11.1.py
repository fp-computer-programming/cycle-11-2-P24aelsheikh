"""

1. Create a Python file named lab_11-1
2. Write a function called find_evens.
3. The function should take in 2 integer values (num_A, num_B), and
return all values found in range(num_A, num_B, 1) that are even.
4. The function needs to be calculated using a for loop and a
conditional statement

""" 
# Author: Alsir Elsheikh
def find_evens(num_A, num_B):
    even_numbers = []

    for num in range(num_A, num_B):
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

# Example usage:
num_A = 10
num_B = 20
result = find_evens(num_A, num_B)
print(result)
