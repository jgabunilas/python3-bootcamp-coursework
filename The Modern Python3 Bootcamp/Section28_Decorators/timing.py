# Let's define a speed_test decorator
from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		# This is a nice line to tell you which function is being executed (decorated), since there are multiple different functions that could be decorated by speed_test
		print(f"Executing {fn.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

# Using a generator function
@speed_test
def sum_nums_gen():
	return sum(x for x in range(90000000))

# Using list comprehension
@speed_test
def sum_nums_list():
	return sum([x for x in range(90000000)])


print(sum_nums_gen())
print(sum_nums_list())

