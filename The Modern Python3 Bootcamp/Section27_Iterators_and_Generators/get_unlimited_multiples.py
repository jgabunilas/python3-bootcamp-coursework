# This generator function takes a number and returns a generator that will yield an unlimited number of multiples of that number


def get_unlimited_multiples(number = 1):
       multiple = 1
       while True:
                yield number * multiple
                multiple += 1

sevens = get_unlimited_multiples(7)


print([next(sevens) for i in range(15)])