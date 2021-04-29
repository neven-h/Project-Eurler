# Euler project Q.No 1

def sum_of_multiplies(n, m):
    mult_sum = 0
    for i in range(3, 1000):
        if i % n == 0 or i % m == 0:
            mult_sum += i
    return mult_sum


print(sum_of_multiplies(3, 5))
# answer: 233168
