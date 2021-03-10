# This function, double_return, returns two copies of the decorated function's return value inside of a list

from functools import wraps

def double_return(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
                result = [fn(*args, **kwargs), fn(*args, **kwargs)]
                return result
        return wrapper

@double_return
def greet(name):
        return "Hi, I'm {}".format(name)

print(greet("Mitch"))