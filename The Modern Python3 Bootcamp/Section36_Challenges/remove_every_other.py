# This function accepts a list as an argument and returns a new list with every second value removed. 

def remove_every_other(input_list):
        # Create a new list that will contain every second value
        new_list = []
        # Generate a list of indices to iterate over. This will be a range from 0 to the length of the input list, stepping by 2 in order to skip every other entry
        indices = range(0, len(input_list), 2)
        # Iterate over the indices list that was generated, and for each index append that member of the input list to the new list
        for index in indices:
                new_list.append(input_list[index])
        return new_list

print(remove_every_other([1,2,3,4,5]))
print(remove_every_other([5,1,2,4,1]))
print(remove_every_other([1]))