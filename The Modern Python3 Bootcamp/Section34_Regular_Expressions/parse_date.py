# This function accepts a string as an argument. The function then checks to see if the string matches a date format. The formats we will recognize are "dd/mm/yyyy", "dd.mm.yyyy", or  "dd,mm,yyyy". The function should return a dictionary containing the three parts of the date with the keys "d", "m", and "y"

import re

def parse_date(input):
        date_regex = re.compile(r'^\b(?P<day>\d{2})[/.,]{1}(?P<month>\d{2})[/.,]{1}(?P<year>\d{4})\b$')
        match = date_regex.search(input)
        # return match.group(3)
        if match:
                return {
                        "d" : match.group('day'),
                        "m" : match.group('month'),
                        "y" : match.group('year')
                }
        return None

print(parse_date("01/22/1999"))
print(parse_date("12,04,2003"))
print(parse_date("12.11.2003"))
print(parse_date("12.11.200312"))