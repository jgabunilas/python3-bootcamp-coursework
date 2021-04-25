# This function accepts a collection, a value, and an optional starting index. The function returns True if the value exists in the collection when searching starting from the starting index. Otherwise, it returns False.

# The collection can be a string, list, or dictionary

def includes(collec, val, start_index = 0):
        
        # check if the collection is a list or string
        if type(collec) == list or type(collec) == str:
                # initialize the search at the start_index
                current_index = start_index

                # Run this while loop until the end of the list/string is reached, or until the loop is exited by the conditions below
                while current_index < len(collec):
                        # check the current index of the collection to see if it matches the desired value. If so, return True and exit the loop and function
                        if collec[current_index] == val:
                                return True
                        # Otherwise, increment the current index by 1 
                        else:
                                current_index += 1
                return False

        # check if the collection is a dictionary
        elif type(collec) == dict:
                # If it is, then iterate over the values of the collection and determine if the value is present
                if val in collec.values():
                        return True
                return False


print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))
print(includes('abcd', 'b'))
print(includes('abcd', 'e'))
print(includes({ 'a': 1, 'b': 2 }, 1))
print(includes({ 'a': 1, 'b': 2 }, 'a'))