# This example illustrates a common use case of decorates that enforces restrictions on arguments. 
# Here, we use a decorator function ensure_no_kwargs to ensure that no keyword arguments are passed into the decorated function greet()

from functools import wraps

def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed! sorry :(")
		return fn(*args, **kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")

greet(name="Tony")






