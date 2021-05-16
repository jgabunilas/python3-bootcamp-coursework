# This function accepts a list of numbers and returns True if any three consecutive numbers sum to an odd number
# Strategy: slice the list in groups of three numbers at a time. The final slice must occur three numbers before the end of the list

def three_odd_numbers(nums_list):
        # Initialize a placeholder index to keep track of where the slice is starting from
        slice_index = 0

        # Iterate through the numbers list.
        for num in nums_list:
                # Ensure that the current slice index is at list 3 numbers away from the end of the list. Otherwise, Python will slice fewer than 3 numbers. 
                if slice_index <= len(nums_list) - 3:
                        # If there are at least 3 numbers left, slice the list to include the number at the current slice index as well as the next two numbers, then sum those numbers together. Remember the the slice is not right-hand inclusive.
                        slice_sum = sum(nums_list[slice_index:slice_index+3])
                        # Test whether the sum is odd. If so, exit the function and return True
                        if slice_sum % 2 != 0:
                                return True
                        slice_index += 1
        # If all slices are summed and none of those sums are odd, return False.
        return False

print(three_odd_numbers([1,2,3,4,5])) 
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0]))
print(three_odd_numbers([5,2,1]))
print(three_odd_numbers([1,2,3,3,2]))

