# This decorator function insures that a keyword argument with the name of "role" and value of "admin" is passed in. otherwise, it will return "Unauthorized"

from functools import wraps


def ensure_authorized(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
                # Loop through each argument in the kwargs dictionary and ensure that one of them has a key of "role" and a value of "admin". If so, return the function so that it can be invoked. 
                for key,value in kwargs.items():
                        if key == "role" and value == "admin":
                                return fn(*args, **kwargs)
                # Otherwise, return "Unauthorized".  Remember that the decorated function will not be invoked if the wrapper does not return it.
                        return "Unauthorized"
        return wrapper

@ensure_authorized
def show_secrets(role):
        return "Shh! Don't tell anybody!"

print(show_secrets(role = "nobody"))
print(show_secrets(role = "admin"))

## Alternative instructor's solution using the .get() method. Remember that .get() returns the value for a keyword in a dictionary. If that keyword is not present, it returns None

# def ensure_authorized(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs.get("role") == "admin":
#             return fn(*args, **kwargs)
#         return "Unauthorized"
#     return wrapper