# This function accepts a list and returns True if each value in the list is a list. Otherwise, the function returns False

def list_check(input):
        for item in input:
                if type(item) is not list:
                        return False
        return True

print(list_check([[], [1], [2,3], (1,2)]))
print(list_check([1, True, [], [1], [2,3]]))
print(list_check([[], [1], [2,3]]))

