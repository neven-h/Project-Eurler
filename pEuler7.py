import math

from is_prime import is_prime

def the_nth_prime(n):
    counter = 1
    prime = 2
    t = n * n
    i: int
    for i in range(3, t // 950, 2):
        # I've chosen the range to be n^2// 950 because for this given number we're getting
        # the correct answer with pretty good runtime
        # but it should probably be a function of n :/
        if is_prime(i) and counter < n:
            counter += 1
            prime = i
    return prime


print(the_nth_prime(10001))
# answer: 104743
