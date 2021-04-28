# Project Euler problem 2
import math


def fibonacci_recu(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recu(n - 1) + fibonacci_recu(n - 2)


# find the index of the fibonacchi number which is our upper bound
def find_fibonacchi_bound():
    k = 5
    bound = 4000000
    while fibonacci_recu(k) < bound:
        k += 1
    else:
        return k


def fibonacci_even_terms():
    upper_range = find_fibonacchi_bound()
    summtion = 0
    fibo_list = []
    for i in range(2, upper_range):
        if fibonacci_recu(i) % 2 == 0:
            fibo_list.append(fibonacci_recu(i))
    summtion = sum(fibo_list)
    print(summtion)


fibonacci_even_terms()
