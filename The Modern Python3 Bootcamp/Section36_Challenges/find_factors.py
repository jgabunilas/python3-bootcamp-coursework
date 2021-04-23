# This function accepts a number and returns a list of all numbers that the number is evenly divisible by, starting with 1 and going up to that number

def find_factors(num):

        # Initialize an empty list of factors
        factors = []

        # Initialize the starting number of 1
        current_number = 1

        while current_number <= num:
                if num % current_number == 0:
                        factors.append(current_number)
                current_number += 1
        return factors

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))
print(find_factors(412146))