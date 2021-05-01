# This function returns True if the sum of each character's position in the alphabet is odd. Indexing starts a 1 - A is at position 1 of the alphabet, not position 0.


def is_odd_string(my_string):
    # Build a dictionary of letters and their positions for the alphabet
    alphabet_dict = {}
    # Provide a string with all letters of the English alphabet
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    # Initialize the first position of the dictionary to 1
    position = 1
    # Iterate over each letter in the alphabet string
    for letter in alphabet_string:
        # Assign that letter as a key in the dictionary and set its value equal to the current position value
        alphabet_dict[letter] = position
        # increment the position by 1
        position += 1

    # Initialize the string_sum that will determine whether the sum is even or odd
    string_sum = 0

    # Iterate over each letter of my_string
    for letter in my_string.lower():
        string_sum += alphabet_dict[letter]

    # Return True if the string_sum is odd (not evenly divisible by 2). Otherwise return False
    return string_sum % 2 != 0

print(is_odd_string('a'))
print(is_odd_string('aaaa'))
print(is_odd_string('amazing'))
print(is_odd_string('veryfun'))
print(is_odd_string('veryfunny'))

# Instructor solution
# def is_odd_string(string):
#     total = sum((ord(c) - 96) for c in string.lower()) or 0
#     return total % 2 == 1