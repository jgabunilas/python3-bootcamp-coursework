# This exercise is a profanity filter. It takes an argument a single string, then censors any word that starts with "frack" with the word "CENSORED".

import re

def censor(input):
        pattern = re.compile(r"""\b(frack) # The word needs to start with frack
        ([a-z]*)\b # after "frack", you you may or may not have additional letters
        """, re.VERBOSE | re.IGNORECASE) # case-insensitive
        result = pattern.findall(input)
        censored = pattern.sub("CENSORED", input)
        return censored

print(censor('Frack you'))
print(censor('I hope you fracking die'))
print(censor('you fracking Frack'))