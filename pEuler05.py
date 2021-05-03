def is_divisible(n):
    for i in range(20, 2, -1):
        if n % i != 0:
            return False
    return True


def smallest_prefect_int():
    k = 27907200  # I chose this number because it's the product of {15,16,17,18,19,20} but is not divisible by 14
    n = k
    temp = k
    while not is_divisible(n):
        n += 10
    else:
        return n


print(smallest_prefect_int())
# answer: 232792560
