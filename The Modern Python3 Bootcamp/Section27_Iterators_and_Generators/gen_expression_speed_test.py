import time

# This illustrates the time it takes to generate a particular list using list comprehension versus generator expressions

# SUMMING 10,000,000 Digits With Generator Expression
# The generator expression performs the summation without creating a list and needing to store it in memory
gen_start_time = time.time() # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time # end time - start time
 
 
# SUMMING 10,000,000 Digits With List Comprehension 
# List comprehension saves the list first, then sums the numbers in the list. It is much more memory-intensive
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")
