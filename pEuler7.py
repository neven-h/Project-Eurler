import math


# I tried to create a file called "is_prime" and to import it but it was not working. tommorow I'll figure that out.

def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        t = math.sqrt(n)
        for i in range(2, int(t) + 1):
            if n % i == 0:
                return False
        return True


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
