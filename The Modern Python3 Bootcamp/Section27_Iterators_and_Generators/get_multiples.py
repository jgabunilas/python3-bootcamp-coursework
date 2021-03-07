# Get multiples exercise
# Accepts a number and a count and returns a generator that yields the first count multiples of the number

def get_multiples(number = 1, count = 10):
        # Initialize the multiple counter
        multiple = 1
        # While the number of multiples is less than or equal to the count, multiply the number by the multiple and yield it. Then increase the multiple by 1
        while multiple <= count:
                yield number * multiple
                multiple += 1

evens = get_multiples(2, 3)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))



## Alternative solution
# In this approach, we control the number of iterations by reducing the count by 1 with each pass through the loop

def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num