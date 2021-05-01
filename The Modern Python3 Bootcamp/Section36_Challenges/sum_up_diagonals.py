# This function accepts an NxN list of lists and sums the two main diagonals in the array, one from the upper left to the lower right, and one from the upper right to the lower left

# The strategy will be to use for loops and increasing index placeholders to iterate over each list and progressively move on index position forward or backward on the next list depending on which diagonal is being summed.

def sum_up_diagonals(matrix):

        # Upper left to lower right sum
        # Initialize an index holder to keep track of the position on each subsequent list. It will start at the 0th position of the first list, then the 1st position of the second list, and so forth
        i = 0
        # Initialize a sum for the top-left to bottom-right diagonal
        first_diag_sum = 0
        # Iterate over each list in the matrix (list of lists) passed in
        for item in matrix:
                # Obtain the value of the ith number in the current list, and add to the diagonal sum
                first_diag_sum += item[i]
                # Then increment the index position by 1
                i += 1

        # Upper right to lower left sum 
        # Start at the last position of the first list
        j = -1
        # Initialize a sum for the top right to bottom left diagonal sum
        second_diag_sum = 0

        # Iterate over each list in the matrix passed in
        for item in matrix:
                # Obtain the value at the jth number in the current list, and add to the diagonal sum
                second_diag_sum += item[j]
                # Then decrement the index position by 1
                j -= 1
        # Sum both diagonals together
        return first_diag_sum + second_diag_sum

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
print(sum_up_diagonals(list1)) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
print(sum_up_diagonals(list2))
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]
print(sum_up_diagonals(list3))

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
print(sum_up_diagonals(list4)) 

# Instructor solution
# def sum_up_diagonals(arr):
#     total = 0
    
#     for i,val in enumerate(arr):
#         total += arr[i][i]
#         total += arr[i][-1-i]
#     return total