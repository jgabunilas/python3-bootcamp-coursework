# This function accepts an array of numbers containing a single duplicate. The function returns that number which is a duplicate, or returns None if there are no duplicates.

def find_the_duplicate(list_values):
        # Iterate through every number in the list
        for number in list_values:
                # Use the .count() method to determine whether there are any duplicates of that number. If a duplicate is encountered, exit the loop and return the number.
                if list_values.count(number) > 1:
                        return number
        # If the entire list is iterated over without encountering a duplicate, return None
        return None

print(find_the_duplicate([1,2,1,4,3,12]))
print(find_the_duplicate([6,1,9,5,3,4,9]))
print(find_the_duplicate([2,1,3,4]))

# Instructor solution
#     def find_the_duplicate(arr):
#         counter = {}
#         for val in arr:
#             if val in counter:
#                 counter[val] += 1
#             else:
#                 counter[val] = 1
#         for key in counter.keys():
#             if counter[key] > 1:
#                 return int(key)