# msg = input("What's the secret password? ")

# while msg != "bananas":
#         print("WRONG!")
#         msg = input("Try again: ")
# print("Correct!")

#  You can also use for loops and while loops interchangably. For example, a for loop can loop over a range.

for num in range(1, 11):
        print(num)

# A while loop can do something similar, but you have to declare a variable and update it each time you go through the loop. If you never update your variable the loop will run forever
num = 1
while num < 11:
        print(num)
        num += 1

