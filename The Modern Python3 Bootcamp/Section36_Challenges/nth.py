# This function accepts a list and a number and returns the element at whatever index is the number in the list. If the number is negative, it will return the nth element from the end. That nth element will always be between the negative value of the list length and the list length minus 1.

def nth(values, nth_index):
        # If the nth_index is 0 or greater, execute the following
        if nth_index >= 0:
                # Check whether the index is within range of the list. If it is, simply return the value at that index
                if nth_index < len(values):
                        return values[nth_index]
                else:
                # Otherwise, state that the index is out of range of the list
                        return "The index is out of range of the list."
        # If the index is negative, execute the following
        else:
                # Check whether the negation of the nth index is shorter than or equal to the length of the list. If so, return the value at the nth position from the end of the list. This index can be obtained by adding the negative nth_index to the length of the list.
                if -nth_index <= len(values):
                        return values[len(values) + nth_index]
                else: 
                # Otherwise, state that the index is out of range of the list

                        return "The index is out of range of the list."

print(nth(['a', 'b', 'c', 'd'], 1))
print(nth(['a', 'b', 'c', 'd'], -2))
print(nth(['a', 'b', 'c', 'd'], 0))
print(nth(['a', 'b', 'c', 'd'], -4))
print(nth(['a', 'b', 'c', 'd'], -1))
print(nth(['a', 'b', 'c', 'd'], 3))
print(nth(['a', 'b', 'c', 'd'], -10))

# Instructor solution
#     def nth(arr, idx):
#         if idx >= 0:
#             return arr[idx]
#         return arr[idx + len(arr)]