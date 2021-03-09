# Exercise
# A function show_args that accepts a function  as an argument and returns a wrapper function.

from functools import wraps

def show_args(fnc):
        @wraps(fnc)
        def wrapper(*args, **kwargs):
                # The args and kwargs from the decorated function are accessible, as is the name of the decorated function that was passed in
                print("Hello, this is {}".format(fnc.__name__))
                print("Here are the args: {}".format(args))
                print("Here are the kwargs: {}".format(kwargs))
                return fnc(*args, **kwargs)
        return wrapper

@show_args
def sample_func(*args, **kwargs):
        pass

sample_func(1, 25, 20, color = "blue", size = "large")