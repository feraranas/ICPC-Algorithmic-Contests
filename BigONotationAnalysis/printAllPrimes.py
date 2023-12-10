'''
(1) is_prime function:

The function checks if a given number n is prime by iterating from 2 to n-1 and 
checking if n is divisible by any of these numbers.

> The loop runs for n - 2 iterations.
> Therefore, the time complexity of the is_prime function is O(n).

(2) print_all_primes function:

The function calls the is_prime function for each element in the input array and prints the prime numbers.

If we denote the length of the input array as m, and the maximum value in the array as max_val, 
the time complexity of print_all_primes is O(m * max_val).
'''

# prime number: a whole number greater than 1 that cannot be exactly divided by any
# whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
def is_prime(n):
     if n < 2:
          return False
     for i in range(2, n):
          if n % i == 0:
               return False
     return True


def print_all_primes(array):
     for k in array:
          if is_prime(k):
               print(k)


print_all_primes([1,2,3,4,5,6])