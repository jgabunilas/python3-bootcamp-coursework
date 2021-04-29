# This function accepts a dictionary and returns a list with the lowest key and the highest key in the dictionary. Assumes that the dictionary will have keys that are numbers

def min_max_key_in_dictionary(dict):

        # Initialize an empty list to hold all keys
        keys = []

        # Iterate over all keys in the dictionary and append each key to the list
        for key in dict.keys():
                keys.append(key)
        # Sort the keys in increasing numerical order
        keys.sort()

        # Return the first (lowest) and last (highest) elements in the sorted list
        return [keys[0], keys[-1]]


                

print(min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}))
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}))