animal = input("Enter your favorite animal")

# The if statement below is equivalent to saying "if animal has a value...". If any value was input for animal, the if statement will resolve to True and the code within the block with run
if animal:
    print(animal + " is my favorite too!")
# If animal is empty, the if statement will not execute and the else statement will run
else:
	print("YOU DIDNT SAY ANYTHING!")
