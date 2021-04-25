# This function accepts two lists of varying lengths. The first list consists of keys and the second one consists of values. The function should return a dictionary created from keys and values. If there are not enough values, the remaining keys should have a value of Null. if there are not enough keys, ignore the remaining values.

def two_list_dictionary(list1, list2):
        # Initialize an empty dictionary
        new_dict = {}
        # Check whether the list of keys is shorter than or equal in length to the list of values
        if len(list1) <= len(list2):
                # If the list of keys is shorter, iterate over each position in the keys list and append new_dict with the key at each position and the value at the same position. Then return the new dictionary
                for position in range(0, len(list1)):
                        new_dict[list1[position]] = list2[position]
                return new_dict
        # If the list of keys is instead longer than the list of values
        else:
                # Iterate over every position in the list of keys
                for position in range(0, len(list1)):
                        # If the current position is smaller than the length of list 2 (that is, if there is a corresponding value in list2 for the key in list1), append new_dict with the key and value at that position
                        if position < len(list2):
                                new_dict[list1[position]] = list2[position]
                        else:
                        # If the current position exceeds the length of values list, append the key at that position with a value of None
                                new_dict[list1[position]] = None 
                return new_dict


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]))
print(two_list_dictionary(['x', 'y', 'z']  , [1,2]))