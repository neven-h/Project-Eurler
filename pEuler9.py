def prod_triplet(n):
    for a in range(1, n):
        for b in range(1, n):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                return a * b * c


print(prod_triplet(1000))
# 31875000, for a = 200, b=375, c = 425
