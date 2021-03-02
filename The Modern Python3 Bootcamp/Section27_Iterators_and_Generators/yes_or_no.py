# A simple generator that vaccilates between returning "yes" and "no"

def yes_or_no():
        condition = 'yes'
        while True:
                yield condition
                if condition == 'yes':
                        condition = 'no'
                elif condition == 'no':
                        condition = 'yes'
        
gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))