# This function accepts two numbers and returns True if they contain the save frequency of digits. Otherwise, it returns False

def same_frequency(num1, num2):
        # Initialize a dictionary to store the numbers and frequencies of num1
        dict1 = {}

        # stringify num1
        num1_str = str(num1)

        # Iterate over each number in the stringified num1. If dict1 already contains that number as a key, add 1 to the value of that key. Otherwise, initialize that key to a value of 1
        for digit in num1_str:
                if digit in dict1:
                        dict1[digit] += 1
                else:
                        dict1[digit] = 1

        # Do the above process for num2
        dict2 = {}
        num2_str = str(num2)
        for digit in num2_str:
                if digit in dict2:
                        dict2[digit] += 1
                else:
                        dict2[digit] = 1

        # Now iterate over the keys in dict1. Compare the values for each key between dict1 and dict2. If they do not match, break out of the loop and return False. Otherwise, return True.
        for num_key in dict1.keys():
                if dict1[num_key] != dict2[num_key]:
                        return False
        return True


print(same_frequency(551122, 221515))
print(same_frequency(321142,3212215))
print(same_frequency(1212, 2211))

# Instructor solution
#     def same_frequency(num1,num2):
#         d1 = {letter:str(num1).count(letter) for letter in str(num1)}
#         d2 = {letter:str(num2).count(letter) for letter in str(num2)}
      
#         for key,val in d1.items():
#             if not key in d2.keys():
#                 return False
#             elif d2[key] != d1[key]:
#                 return False
#         return True