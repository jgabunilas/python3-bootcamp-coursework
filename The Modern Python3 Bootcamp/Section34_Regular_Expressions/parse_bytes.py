# This function accepts a single string and returns a list of the binary bytes contained within the string. Each byte is just a combination of either 1s or 0s

import re

def parse_bytes(input):
        bytes_regex = re.compile(r'\b[01]{8}\b')
        match = bytes_regex.findall(input)
        return match

print(parse_bytes('11010101'))
print(parse_bytes('my data is: 10101010 11100010'))
print(parse_bytes(('asdsa')))
