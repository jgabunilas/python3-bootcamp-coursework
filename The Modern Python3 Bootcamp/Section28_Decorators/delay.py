# In this exercise, the wrapper function delay() will delay execution of the decorated function for the amount of time (in seconds) passed into it

from functools import wraps
from time import sleep

# Start by defining the decorated function delay() with "time" as a parameter
def delay(time):
        # Define the inner function which accepts the decorated function as its argument
        def inner(func):
                @wraps(func)
                # Define the wrapper function that takes the arguments from the decorated function and performs the decoration on it
                def wrapper(*args, **kwargs):
                        print("Waiting {}s before running {}".format(time, func.__name__))
                        sleep(time)
                        # Return the decorated function
                        return func(*args, **kwargs)   
                # Return the wrapper   
                return wrapper 
        # Return the inner
        return inner

@delay(3)
def say_hi():
        return "Hi!"

print(say_hi())
