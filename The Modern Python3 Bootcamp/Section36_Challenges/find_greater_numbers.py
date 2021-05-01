# This function accepts a list and returns the number of times a number if followed by a larger number across the entire list

def find_greater_numbers(nums_list):

        # Initialize a counter that keeps track of the current index of the number being tested. This will be incremented by 1 each time we move to the next number on the list.
        current_index = 0

        # Initialize a counter that counts how many times the number we are testing is followed by a larger number across the remainder of the list
        larger_numbers = 0

        # Iterate through every number in the list. This is the "number under test"
        for num in nums_list:
                # print(f"Currently testing {num}")

                # Create a range of indices that we will iterate over. This range starts at the index of the current number being tested and goes to the index of the last number in the list. Remember that the range will end at len(nums_list) - 1 since the last position is non-inclusive. The range will be get progressively smaller for each number, decreasing in size by 1 until we reach the last number in the list
                index_range = range(current_index, len(nums_list))

                # Iterate over each index in the range of indices
                for index in index_range:
                        # Check whether the number under test is lower than the number at the current index. If so, increment the larger_numbers counter by 1
                        if num < nums_list[index]:
                                # print(f"{num} is less than {nums_list[index]}")
                                larger_numbers += 1
                # When moving on to the next number to test, increment the current_index by 1 so that the range of indices for the next number is smaller by 1
                current_index += 1
        # Return the larger_numbers count
        return larger_numbers




print(find_greater_numbers([6,1,2,7]))
print(find_greater_numbers([1,2,3]))
print(find_greater_numbers([5,4,3,2,1]))
print(find_greater_numbers([]))