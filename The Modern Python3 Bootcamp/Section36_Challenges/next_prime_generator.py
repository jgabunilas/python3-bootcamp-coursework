# This function, next_prime, returns a generator function that will yield an unlimited number of prime numbers, starting from the first prime number.
# A prime number is any whole number that has exectly two divisors, 1 and the number itself

def next_prime():
        test_number = 2
        while True:
                # print('current test number is', test_number)
                if test_number == 2:
                        yield test_number
                        test_number += 1
                else:
                        # print('current test number is', test_number)

                        # No even numbers except 2 are prime. If the number is even, increment the test number by 1 and move to the next iteration of the while loop
                        if test_number % 2 == 0:
                                test_number += 1
                        
                        # If the number is odd then we must test it for prime-nexx
                        else:
                                # Create a range of possible factors spanning from 2 to the number right before the current test_number
                                for possible_factor in range(2, test_number):
                                        # print('possible factor for test number', test_number,':', possible_factor)

                                        # Iterate through each possible factor. If the test_number is evenly divisible by the possible factor, then the test_number is not prime. Increment the test_number by 1 and break out of the factor for loop in order to move to the next ieration of the while loop
                                        if (test_number % possible_factor == 0):
                                                test_number += 1
                                                break

                                        # If the possible factor being tested is the last number in the factors list and the test_number is not evenly divisible by that factor, then the text_number is prime. Yield that number, then increment test_number by 1
                                        elif (possible_factor == test_number - 1) and (test_number % possible_factor != 0):
                                                # print(test_number, 'is a prime number')
                                                yield test_number
                                                test_number += 1

                        

primes = next_prime()
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))
# print(next(primes))

print([next(primes) for i in range(25)])

# Instructor solution
#     def next_prime():
#         num = 2
#         all_primes = set()
#         while True:
#             for prime in all_primes:
#                 if num % prime == 0:
#                     break
#             else:
#                 all_primes.add(num)
#                 yield num
#             num += num % 2 + 1
