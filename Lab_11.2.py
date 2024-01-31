"""
2. Write a function named is_palindrome.
3. The function should take in string, and return a boolean value
indicating whether or not the string is a palindrome.
4. The function needs to work regardless of additional spaces or
capitalization.
"""
# Author: Alsir Elsheikh
def is_palindrome(input_str):
    # Convert the input string to lowercase and remove spaces
    cleaned_str = ''.join(input_str.lower().split())

    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
test_string = "A man a plan a canal Panama"
result = is_palindrome(test_string)

if result:
    print(f'The string "{test_string}" is a palindrome.')
else:
    print(f'The string "{test_string}" is not a palindrome.')
