# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.
 
import itertools                                             #Import the module itertool

primes_below_number = 2000000        
numbers = [v % 2 !=0 for v in range(primes_below_number)]    # All the even numbers are eliminated and the odd numbers are storedin 
numbers[0] = False                                           # An array called numbers .
numbers[1] = False                                           # Iterates n starting from 9,12,15 etc and eliminates those indexes                                                   from numbers array(i.e give those indexes as false)                                                                                             
numbers[2] = True

number = 3
itertools.imap = lambda*args,**kwargs: list(map(*args,**kwargs))

while number < primes_below_number:
    n = number*3                                             # We already excluded even numbers
    while n < primes_below_number:
        numbers[n] = False
        n += number
    number += 1
    while number < primes_below_number and not numbers[number]:
        number += 1
sum_of_numbers = sum(itertools.imap(lambda index_n:index_n[1] and index_n[0] or 0, enumerate(numbers)))
print (sum_of_numbers)                                      # Take sum of the rest of the values in numbers array and the prime number
                                                            # Which is less than 9
