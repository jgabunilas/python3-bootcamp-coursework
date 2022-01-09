# This function returns a function that, when passed a value, returns the current average of all previous function calls. That is, it keeps a running average.

def running_average():
        # Define the variables for total numbers counted and the running total. Remember that since these variables are defined in the enclosing function, all nested functions will be able to reference them and modify then, and they will be "remembered" during future calls to the nested function.
        total_nums = 0
        total = 0

        # Define the nested function which will do all the heavy lifting. 
        def averager(number):
                # In order to access the total and total_nums variables from the enclosing function, they must be defined as nonlocal here so that the nested function knows to refer to previously bound variables in the nearest enclising scope.
                nonlocal total
                nonlocal total_nums

                # Increment the total number of numbers by 1 each time the nested function is called.
                total_nums += 1

                # Increment the running total by the value of the number passed in. 
                total += number
                return round(total / total_nums, 2)

        # The nested function must be returned when the enclosign function is called
        return averager

rAvg = running_average()
print(rAvg(10)) # 10.0
print(rAvg(11)) # 10.5
print(rAvg(12)) # 11

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2
