import time
import math


# from sieve_is_prime import make_sieve


def find_number_with_n_divisors(n):
    counter = 1
    x = 2
    n + 1
    counter = how_many_divisors(x)
    while counter < n:
        x += 1
    return counter


# print(find_number_with_n_divisors(120)
def prime_factors(n):
    divisors_list = []
    # even number divisible
    while n % 2 == 0:
        divisors_list.append(2)
        # print(2)
        n = n / 2
    # n became odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            divisors_list.append(i)
            # print(i)
            n = n / i
    if n > 2:
        # print(n)
        divisors_list.append(n)
    return divisors_list


# n = int(input("Enter the number for calculating the prime factors :\n"))
# print(prime_factors(514880))


# 70600674
def how_many_divisors(n):
    divisors_counter = 1
    prime_divisors = prime_factors(n)
    number_of_divisors = 1
    i = 0
    while i + 1 < len(prime_divisors):
        if prime_divisors[i] == prime_divisors[i + 1]:
            i += 1
            divisors_counter += 1
        else:
            i += 1
            number_of_divisors *= divisors_counter
    return number_of_divisors

#
# print(prime_factors(65453))
#
# print(how_many_divisors(5780))
print(prime_factors(56))

print(how_many_divisors(56))


print(8*3*7)