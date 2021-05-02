from sieve_is_prime import make_sieve


def number_of_primes(sieve):
    return sum(sieve)


def sieve_n_primes(n):
    sieve = [0]
    while number_of_primes(sieve) < n:
        sieve = make_sieve(10 * len(sieve))
    return sieve


def is_prime_using_sieve(sieve, n):
    if sieve[n] == 1:
        return True
    return False


def nth_prime(n):
    counter = 1
    prime = 2
    i = 3
    sieve = sieve_n_primes(n)
    while counter < n:
        if is_prime_using_sieve(sieve, i):
            counter += 1
            prime = i
        i += 1
    return prime


print(nth_prime(10001))
