import math


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        t = math.sqrt(n)
        for i in range(2, int(t)+1):
            if n % i == 0:
                return False
        return True


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
