# This function accepts a list of numbers and returns the most frequent number (the mode) in the list of numbers. Assume that the mode will be unique.
# Strategy: Store all numbers in a dictionary and keep a running count for all of those numbers. When all numbers and counts have been stored, return the number with the highest count.

def mode(nums_list):
        # Initialize an empty dictionary that will hold each number and their count
        nums_dictionary = {}
        # Iterate through each numberin the list. If the number is no in the dictionary, add it as a key and initialize its value to 1. If the number is already in the dictionary, increment its value by 1.
        for num in nums_list:
                if num not in nums_dictionary:
                        nums_dictionary[num] = 1
                else:
                        nums_dictionary[num] += 1
        print(nums_dictionary)

        # Create a list containing all of the keys in the nums_dictionary
        nums_keys = list(nums_dictionary.keys())

        # Initialize a mode count against which the mode candidates (the keys in the nums_dictionary) will be tested. This can be initialized to zero, since any candidate that appears at least once in the list will have a count that is greater than this.
        mode_count = 0
        
        # Iterate through each key in the nums_keys list and check whether the value (i.e. count) for that key in the nums_dictionary is greater than the current mode_count. If it is, update the mode_num to the current num_key being tested, and update the mode_count to the value of that num_key
        for num_key in nums_keys:
                if nums_dictionary[num_key] > mode_count:
                        mode_num = num_key
                        mode_count = nums_dictionary[num_key]

        # Finally, return the mode
        return mode_num

# Another student's solution, much more elegant!
# def mode(nums):
#   result = 0
#   for num in set(nums):
#     if nums.count(num) > result:
#       result = num
#   return result


print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))
print(mode([3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]))