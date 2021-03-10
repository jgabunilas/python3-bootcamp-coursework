# In this exercise, a decorator function ensures that the decorated function has only three or fewer arguments passed into it


def ensure_fewer_than_three_args(fn):
        def wrapper(*args, **kwargs):
                # If there are more than 3 arguments, return a message stating as such
                if (len(args) + len(kwargs)) > 3:
                        return "Too many arguments!"
                # Otherwise, return the decorated function
                return fn(*args, **kwargs)
        return wrapper

@ensure_fewer_than_three_args
def add_all(*args):
        return sum(args)

print(add_all(1,2,3))
print(add_all(1,2))
print(add_all(1,2,3,4,5,6))
