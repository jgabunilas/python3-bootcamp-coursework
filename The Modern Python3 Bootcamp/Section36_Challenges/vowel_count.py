# This function accepts a string and returns as a dictionary the keys as vowels and the count of the vowels as values

def vowel_count(input_string):
        # define a tuple with all vowels
        vowels_tup = ('a', 'e', 'i', 'o', 'u')

        # initialize an empty dictionary to hold the vowel counts
        vowel_dict = {}

        # Iterate through each letter in the input string
        for letter in input_string:
                # Test whether the letter is a vowel. Apply the lower() method to ensure the both capitalized and lower-case version of the vowel are accounted for as the same letter
                if letter.lower() in vowels_tup:
                        # If so, check the vowel dict to see if the vowel is already a key
                        if letter.lower() in vowel_dict.keys():
                                # If the vowel is already in the dictionary, then increment the count by 1
                                vowel_dict[letter.lower()] += 1
                        else:
                                # Otherwise, add the vowel as a key to the dictionary 
                                vowel_dict[letter.lower()] = 1
        return vowel_dict

print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))

# Instructor's solution utilizing dictionary comprehension and the .count() method
#     def vowel_count(string):
#         lower_s = string.lower()
#         return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


