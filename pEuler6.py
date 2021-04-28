import math


def square_of_sum(n):
    t = 0
    for i in range(1, n + 1):
        t += i
    return t * t


def sum_square(n):
    square_list = []
    for i in range(1, n + 1):
        square_list.append(i * i)
    return sum(square_list)


p = square_of_sum(100)
m = sum_square(100)

print(p - m)
