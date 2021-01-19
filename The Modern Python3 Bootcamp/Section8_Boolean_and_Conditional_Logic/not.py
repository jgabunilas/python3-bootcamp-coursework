# movie ticket example for the not statement
age = 70
# age 2-8: $2 ticket
# age 65+: $5 ticket
# any other age: $10 ticket

# check if age is between 2 and 8 OR if age is greater than 65. If either is true, then it will resolve to True
(age >=2 and age <=8) or age >= 65

# if we throw a "not" in front of the statement, then if either is True, it will resolve to False. If both are False, then it will resolve to True. Age 21 is neither between 2 and 8 nor greater than 65, so the statement in parentheses will resolve to False. With the "not" in front of it, the statement will resolve to True, and the containing code will be run
if not ((age >=2 and age <=8) or age >= 65):
        print("You pay $10 and are not a child or senior")
else:
        print('You are a child or senior')

# This evaluates to False
print(not 1 < 2)
# This evaluates to True
print(not (1 > 3 and 5 == 5))