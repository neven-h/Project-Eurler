from sieve_is_prime import make_sieve


# this function creates a sieve for all prime numbers smaller then n
def sieve_of_n_prime_numbers(n):
    sieve = [0]
    while len(sieve) < n:
        sieve = make_sieve(10 * len(sieve))
    return sieve


# if sieve[n] is a prime number the function returns true
def is_n_prime_using_sieve(sieve, n):
    if sieve[n] == 1:
        return True
    return False


# this function calculates the sum of prime number using the sieve
def sum_of_primes(n):
    i = 3
    primes_sum = 2
    sieve = sieve_of_n_prime_numbers(n)
    while i < n:
        if is_n_prime_using_sieve(sieve, i):
            primes_sum += i
            prime = i
        i += 1
    return primes_sum


print(sum_of_primes(2000000))
# 142913828920
