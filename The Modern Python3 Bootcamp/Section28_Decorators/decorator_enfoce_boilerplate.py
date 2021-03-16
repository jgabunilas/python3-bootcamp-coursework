# Use this boilerplate code for creating decorators that accept values for their decoration tasks

from functools import wraps

def decorator_function(value):
        # Define the inner function which accepts the decorated function as its argument
        def inner(func):
                @wraps(func)
                # Define the wrapper function that takes the arguments from the decorated function and performs the decoration on it
                def wrapper(*args, **kwargs):
                        # Do your thing
                        # Return the decorated function
                        return func(*args, **kwargs)   
                # Return the wrapper   
                return wrapper 
        # Return the inner
        return inner