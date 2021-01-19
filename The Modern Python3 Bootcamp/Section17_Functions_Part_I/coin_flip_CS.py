from random import random

def flip_coin():
    # Remember that random returns a random value between 0 and 0.99(repeating)
    # if the returned value is greater than 0.5, return 'heads'
	if random() > 0.5:
		return "HEADS"
    # Otherwise, return 'tails'
	else:
		return "TAILS"

print(flip_coin())


