import math
from is_prime import is_prime
from pEuler7 import the_nth_prime


def prime_divisors(n):
    max_prime = 2
    if is_prime(n):
        return n
    else:
        t = int(math.sqrt(n))
        for k in range (the_nth_prime(1000), the_nth_prime(10000), 2): #the 1000th prime number is not a divisor of n,
            # the_nth_prime(10000) is some upper bound I've chosen and improves performances significantly but I wonder
            # if there is some closed formula for a lower and upper bound for this problem
        #for k in range(1051, t // 2, 2):  # I've chosen to start from 1051 which is prime and is not a divisor of 600851475143
            if is_prime(k):
                if n / k == int(n / k) and k > max_prime:
                    max_prime = k
        return max_prime


print(prime_divisors(600851475143))
