# This function accepts a string and returns a function. When the inner function is invoked, it accepts a parameter which is a letter, and the inner function returns the number of times that letter appears. The inner function should be case insensitive.

def letter_counter(input_str):

        def inner_func(letter):
                return input_str.lower().count(letter)
        return inner_func

counter = letter_counter("Amazing")
print(counter('a'))
print(counter('m'))

counter2 = letter_counter("This Is Really Fun!")
print(counter2('i'))
print(counter2('t'))