# Project Euler problem 2
import math

fib_usage_counter = 0


# def fibonacci_recu(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recu(n - 1) + fibonacci_recu(n - 2)

# calculating the Fibonacci sequence without recursion
def fib(n: int) -> int:
    global fib_usage_counter
    if n == 0: return 0
    value1, value2 = 1, 1
    while n > 2:
        fib_usage_counter += 1
        value1, value2 = value2, value1 + value2
        n -= 1
    return value2


# find the index of the Fibonacci number which is our upper bound
def find_fibonacci_bound():
    k = 5
    bound = 4000000
    while fib(k) < bound:
        k += 1
    else:
        return k


def fibonacci_even_terms():
    upper_range = find_fibonacci_bound()
    fibonacci_sum = 0
    for i in range(2, upper_range):
        if fib(i) % 2 == 0:
            fibonacci_sum += fib(i)
    print(fibonacci_sum)


print(fibonacci_even_terms())
print(f'fib_usage_counter: {fib_usage_counter}')
# fib_usage_counter: 73
