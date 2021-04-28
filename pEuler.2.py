def is_prime(p):
    if p % 2 == 0:
        return False
    else:
        for i in range(2, (p // 2 + 1)):
            if p % i == 0:
                return False
        return True


def prime_divisors(n):
    max_prime = 2
    if is_prime(n):
        return n
    else:
        for k in range(3, (n // 2 + 1), 2):
            if is_prime(k):
                if n / k == int(n / k) and k > max_prime:
                    max_prime = k
        return max_prime
print(prime_divisors(600851475143))
