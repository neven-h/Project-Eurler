import math
from is_prime import is_prime

def prime_divisors(n):
    max_prime = 2
    if is_prime(n):
        return n
    else:
        t = int(math.sqrt(n))
        for k in range(3, t , 2):
            if is_prime(k):
                if n / k == int(n / k) and k > max_prime:
                    max_prime = k
        return max_prime


print(prime_divisors(600851475143))
