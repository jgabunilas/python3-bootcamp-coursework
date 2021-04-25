# This function shortens an input string to a specified length, adding ... to the end. It accepts a string and a number, and truncates the string to a shorter string containing at most n characters, returning that string. If the string gets truncated to n characters, then the returned string should have "..." at the end. The "..." should be counted as part of the n characters. Because of this, the number n passed in should be 3 or greater.

def truncate(input_string, n):

        # Check if the number of characters truncated to is less than 3 characters. If it is, return a message that a truncations can only be 3 characters or greater
        if n < 3:
                return "Truncation must be at least 3 characters."
        else:
                # Check the length of the string and add 3 to it to account for the "...". If this value is less than or equal to the truncation value n, return the string unaltered.
                if len(input_string) + 3 <= n:
                        return input_string
                
                # If the length of the string plus 3 is greater than the truncation value, slice the string from the start to 3 positions prior to the truncation value, to account for the "...". Then append "..." to the end of that string
                else:
                        return input_string[0:n-3] + '...'

print(truncate("Super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Super cool", 0))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Another test", 12))
print(truncate("Woah", 4))
print(truncate("Woah", 3))
print(truncate("Yo",100))
print(truncate("Holy guacamole!", 152))
