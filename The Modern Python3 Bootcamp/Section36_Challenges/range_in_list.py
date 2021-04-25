# This function accepts a list of numbers and start and stop indices, and returns the sum of values between and including the start and stop index.
# If a start parameter is not provided, it defaults to zero (0). If an end parameter is not passed in, it should default to the last value in the list
# If the end index is larger than the length of the list, the function should still go to the end of the list

# def range_in_list(nums_list, start_index = 0, end_index = 0):
#         # If an end index was not passed into the argument and defaults to 0, update the end index to the length of the nums_list.
#         if end_index == 0:
#                 end_index = len(nums_list)
        
#         # Initialize a sum_total value to 0
#         sum_total = 0
#         # Create an iterable of index numbers with which to pull values from the nums_list. The index numbers will go from the start_index and end at the end_index plus 1Remember that by default, the range function creates a list of integers that from the start number and up to but not including the end number. Since we want the end index to be included in the sum, we must add 1 to the end_index.
#         for num in range(start_index, end_index + 1):
#                 sum_total += nums_list[num]
#         return sum_total

def range_in_list(nums_list, start_index = 0, end_index = 0):
        # If an end index was not passed into the argument and defaults to 0, update the end index to the length of the nums_list.
        if end_index == 0:
                end_index = len(nums_list)
        
        # Initialize a sum_total value to 0
        sum_total = 0
        # Create a new list consisting of a slice of nums_list starting from the start_index and ending at the end_index plus 1. Remember that because by default slicing goes up to but does not include the last value of the slice, in order to slice to the desired end_index, we must add 1 to the slice end value.
        sliced_num_list = nums_list[start_index:end_index+1]
        for num in sliced_num_list:
                sum_total += num
        return sum_total

print(range_in_list([1,2,3,4],0,2))
print(range_in_list([1,2,3,4],0,3))
print(range_in_list([1,2,3,4],1))
print(range_in_list([1,2,3,4]))
print(range_in_list([1,2,3,4],0,100))
print(range_in_list([],0,1))

# Instructor solution
#     def range_in_list(lst, start=0, end=None):
#         end = end or lst[-1]
#         return sum(lst[start:end+1])