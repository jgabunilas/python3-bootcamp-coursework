# This function takes a list of numbers as its argument and returns the two hihgest numbers within the list. The numbers are passed in in any order.

def two_oldest_ages(nums_list):
    # sort the list in ascending order
    nums_list.sort()

    # return a list consisting of the last two members of the sorted list
    return [nums_list[len(nums_list) - 2], nums_list[len(nums_list) - 1]]
    # Alternative return statement using slicing
    # return nums_list[-2:len(nums_list)]
        
print(two_oldest_ages([1, 2, 10, 8]))
print(two_oldest_ages([6,1,9,10,4]))
print(two_oldest_ages([4,25,3,20,19,5]))

# Instructor solution
# def two_oldest_ages(ages):
#     return sorted(ages)[-2:]