def is_divisible(n):
    for i in range(20, 2, -1):
        if n % i != 0:
            return False
    return True


def smallest_prefect_int():
    k = 9699690
    n = k
    temp = k
    while not is_divisible(n):
        n += 10
    else:
        return n


print(smallest_prefect_int())

