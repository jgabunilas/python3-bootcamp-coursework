# In the example below, num1 assumes the value of the first argument passed into the function
def prac_func(num1, *args):
        sum = 0
        for num in args:
                sum += num
        return sum

print(prac_func(100, 1, 1, 1, 1)) # 4

def prac_func2(num1, *args):
        sum = 0
        sum += num1
        for num in args:
                sum += num
        return sum

print(prac_func2(100, 1, 1, 1, 1)) # 104
