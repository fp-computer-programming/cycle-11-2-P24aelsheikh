"""
1. Create a Python file named lab_11-8.py
2. Write a program that contains a function called
length_multiples. The function should take a list as its only
parameter.
3. The function should create a new list, where each new value is the
original value multiplied by its index.
4. The function should return the new list
5. Write 3 test cases to confirm that your function works when passed
a list that:
1. Contains only integers
2. Contains integer and float values
3. Contains only strings
"""
# Author: Alsir Elsheikh

def length_multiples(input_list):
    new_list = [value * index for index, value in enumerate(input_list)]
    return new_list

# Test case 1: Contains only integers
test_list1 = [1, 2, 3, 4, 5]
result1 = length_multiples(test_list1)
print("Test Case 1:", result1)

# Test case 2: Contains integer and float values
test_list2 = [1, 2.5, 3, 4.2, 5]
result2 = length_multiples(test_list2)
print("Test Case 2:", result2)

# Test case 3: Contains only strings
test_list3 = ["a", "b", "c", "d", "e"]
result3 = length_multiples(test_list3)
print("Test Case 3:", result3)
