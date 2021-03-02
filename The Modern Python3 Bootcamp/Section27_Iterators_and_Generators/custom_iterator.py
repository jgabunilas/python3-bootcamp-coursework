class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	# In order to make something an iterable, we must make it responsive to an iter() function that returns an iterator. Here we define how Counter class response to having iter() called on it
	def __iter__(self):
		return self

	# But that's not enough to get the functionality we need. We need to define the behavior of the next() function, which is called on the iterator
	def __next__(self):
		if self.current < self.high:
			# Note the order here. We're returning num, but in order to add 1 to current each time through the loop, we need to update self.current before returning the CURRENT num. If we were to put the return statement before self.current += 1, we would never increase self.current
			num = self.current
			self.current += 1
			return num
		raise StopIteration



# In the for loop below, remember that behind the scenes, iter() is being called on Counter
for x in Counter(50,70):
	print(x)