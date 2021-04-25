# This function accepts a string and a number and returns a new string with the string passed to the function repeated the number amount of times. 

def repeat(input_str, num_repeats):
        return input_str * num_repeats

print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))