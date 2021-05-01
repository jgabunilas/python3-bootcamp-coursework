# This function accepts a string of parentheses and returns True if the order of the parentheses is value. Otherwise it returns False
# A valid set of parentheses meets the following criteria: (1) starts with an open paren, (2) has an equal number of open and close parens, and (3) every open paren is balanced by a close paren further down in the string

def valid_parentheses(paren_string):

    # First record the indices for the first opening and first closing parens
    first_open = paren_string.find('(')
    first_close = paren_string.find(')')

    # First check that the number of open and close parens is the same. This is requirement for a valid set of parentheses. If it isn't, return False
    if paren_string.count('(') != paren_string.count(')'):
        return False
    # If the first close parentheses comes before the first open parentheses, then this is also invalid. Return False
    elif first_close < first_open:
        return False
    # If both conditions above are met, we must now ensure that each open paren is followed by at least one close parent
    else:
        # Initialize a value that carries the index of the current character being evaluated
        current_index = 0
        # Iterate through each character in paren_string
        for char in paren_string:
            # If the character is an open paren, we must then check to ensure that there is at least one close paren further down in the string. 
            if char == "(":
                # Use the .find() method to search for a close paren, starting from the current index and going until the end of the string. If a close paren is not encountered, this method will return -1. If that is the case, the parentheses string is invalid and should return False
                if paren_string.find(')', current_index, len(paren_string)) == -1:
                    return False
            current_index += 1
        # Otherwise, all criteria for a valid parentheses string are satisfied and the fucntion should return True
        return True




print(valid_parentheses("()"))
print(valid_parentheses(")(()))"))
print(valid_parentheses("("))
print(valid_parentheses("(())((()())())"))
print(valid_parentheses('))(('))
print(valid_parentheses('())('))
print(valid_parentheses('()()()()())()('))

# valid_parentheses("()") # True 
# valid_parentheses(")(()))") # False 
# valid_parentheses("(") # False 
# valid_parentheses("(())((()())())") # True 
# valid_parentheses('))((') # False
# valid_parentheses('())(') # False
# valid_parentheses('()()()()())()(') # False