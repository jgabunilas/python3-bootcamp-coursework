# A decorator function that ensures the decorated function is called with only integers
from functools import wraps

def only_ints(fn):
        @wraps(fn)
        def wrapper(*args):
                # Loop through each argument in the args tuple and ensure it is an integer. If a non-integer argument is encountered, return a statement asking to invoke the function with integers. Remember that the return statement will exit the loop and the wrapper function
                for arg in args:
                        if type(arg) != int:
                                return "Please only invoke with integers."
                # Otherwise, return the decorated function
                return fn(*args)
        return wrapper

@only_ints
def my_func(*args):
        return args

print(my_func(1,2))
print(my_func('test',2))

## Alternative solution using the built-in any function and list comprehension
# def only_ints(fn):
#     @wraps(fn)
#     def inner(*args, **kwargs):
#         if any([arg for arg in args if type(arg) != int]):
#             return "Please only invoke with integers."
#         return fn(*args, **kwargs)
#     return inner
