# an function that return an array
def make_sieve(n):
    sieve = [1] * n
    sieve[0:1] = [0, 0]
    p = 0
    while p < n:
        if sieve[p] == 1:
            for i in range(2 * p, n, p):
                sieve[i] = 0
        p += 1
    return sieve


# arr_prime = []
# for i in range(21):
#     assert is_prime(i) == bool(arr[i]), i
