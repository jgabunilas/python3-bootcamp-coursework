# This function accepts a list and a number and returns the first pair of numbers that sum to the number passed to the function

def sum_pairs(nums_list, number):
        # Initialize a list of indices that will be iterated over. These indices should include all numbers from 0 up to the length but not including the length of the nums_list
        index_iterator = range(0, len(nums_list))

        # Initialize an empty list that the pair of numbers will be added to
        sum_pair = []

        # Iterate over each index
        for index in index_iterator:
                # Check to ensure that the current index plus 1 is less than the length of the nums_list.
                if index + 1 < len(nums_list):
                        # If the current index plus 1 is less than the length of the nums_list, then there is still at least one index following the current one that can be accessed. Sum the numbers at the current and next index.
                        if nums_list[index] + nums_list[index + 1] == number:
                                # If the sum is equal to the desired number, then append the number a the current index and the number at the next index to the sum_pair list. Then return that list and exit the function
                                sum_pair.append(nums_list[index])
                                sum_pair.append(nums_list[index + 1])
                                return sum_pair
        # If the entire for loop runs without the sum being achieved by two consecutive numbers, simply return the empty sum_pair list
        return sum_pair

print(sum_pairs([4,2,10,5,1], 6))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
print(sum_pairs([11,20,4,2,1,5], 24))

