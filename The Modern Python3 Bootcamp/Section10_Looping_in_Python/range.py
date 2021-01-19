# prints 0 through 9
for num in range(10):
        print(num)

print('')

# prints even numbers from 10 to 20 (exclusive of 20)
for num in range(10,20,2):
        print(num)

print('')

# sums every odd number from 10 to 20 and stores result in the variable x
x = 0
for number in range(11, 20, 2):
        x += number
        print(x)