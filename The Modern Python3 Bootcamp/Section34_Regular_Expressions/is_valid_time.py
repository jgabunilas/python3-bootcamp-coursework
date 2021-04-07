# This expression takes a single string as an argument. It returns True if the string is correctly formatted as a time. Otherwise it returns false. Times can start with a single number or two numbers

import re

def is_valid_time(timestring):
        # Create the regex pattern and compile it
        pattern = re.compile(r'\d?\d:\d\d')
        result = pattern.fullmatch(timestring)
        if result:
                return True
        return False

print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:23"))
print(is_valid_time("it is 12:15"))
print(is_valid_time("12:15"))

## Alternative solution using anchors
# import re 

# def is_valid_time(input):
# pattern = re.compile(r'^\d\d?:\d\d$')
# match = pattern.search(input)
# if match:
#         return True
# return False



