# This function accepts a functio nand returns a new function that can only be invoked once. If the function is invoked more than once, it should return None. 
# Strategy: Define a new function inside the once function and return that function. This inner function contains the logic that decides whether to execute the passed in function or to return None

# Define the function that will be passed into once
def add(add1, add2):
        return add1 + add2

def subtract(num1, num2):
        return num1 - num2
        
# Define the once function, which accepts a function as an argument and ensures that function is only executed once
def once(func):
        # Create a nonlocal variable that tracks whether the passed in function has been executed
        executed = False

        # Define the inner function, which controls the execution of the passed in function. Since the number of arguments passed to the inner function can change depending on the number of arguments needed for function that is passed in, we'll need to accommodate those arguments as *args
        def inner(*args):
                # Declare the executed variable as nonlocal so that the inner function can access its value from the once function
                nonlocal executed

                # If executed is false, set executed to true and then return the passed in function with its original arguments. You can use *args for this
                if executed == False:
                        executed = True
                        return func(*args)
                # If executed is not false, return None
                else:
                        return None   
        # Return the inner function                   
        return inner
        
oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None

oneSubtraction = once(subtract)
print(oneSubtraction(10,5)) # 4
print(oneSubtraction(2,2)) # None
print(oneSubtraction(12,200)) # None




