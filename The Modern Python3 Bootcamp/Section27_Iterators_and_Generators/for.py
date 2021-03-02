# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"

# When calling our dumbed-down for loop function, you will want to pass in an iterable as well as a function to run on each element of the iterator
def my_for(iterable, func):
	# Create the iterator on the iterable by calling the iter() function
	iterator = iter(iterable)

	# Use a while loop here. Why? Because you generally want to continue iterating until you no longer can
	while True:
		# Use a try/except block to break from the loop if next() cannot be called
		try:
			thing = next(iterator)
		except StopIteration:
			break
		# The func() call does not need to be an else clause, it was just shown as such here to make the code clearer. The func() call could be within the try block
		else:
			func(thing)
		
def square(x):
	print(x*x)

# remember that print() is a built-in function. No need to define it
my_for("lol", print)
my_for([1,2,3,4,5], square)
