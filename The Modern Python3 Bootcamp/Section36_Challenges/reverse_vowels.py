# This function reverses the vowels (excluding y) in a string. That is, the first vowel should become the last vowel, etc. Consonants are to be unchanged.
# Strategy: store the vowels for the string in a new list, then reverse that list. When reconstructing the string, utilize a for loop to check whether the next character is a vowel. If so, pull from the next character in the reversed list. If not, pull from original string.

def reverse_vowels(input_str):

        # Initialize an empty list to hold the vowels
        vowels_list = []

        # Iterate through the input string and check if the letter is a vowel. If so, add it to the list of vowels

        for letter in input_str:
                if letter.lower() in ['a','e','i','o','u']:
                        vowels_list.append(letter)
        
        # Reverse the vowels_list in place
        vowels_list.reverse()

        # Initialize an empty string to be reconstructed
        reversed_vowels_str = ''

        # Create an index to keep track of your "place" in the reversed vowel list
        vowels_list_index = 0

        # Iterate over each letter of the input string and for each letter determine whether it is a vowel. If so, pull the next vowel from the reverse vowel list. If not, pull then ext letter of the input string
        for letter in input_str:
                if letter.lower() in ['a','e','i','o','u']:
                        reversed_vowels_str += vowels_list[vowels_list_index]
                        vowels_list_index += 1
                else:
                        reversed_vowels_str += letter
        
        # Return the string with the vowels reversed
        return reversed_vowels_str

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))


