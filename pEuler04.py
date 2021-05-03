def compare_digits():
    max_palindrom = 500000
    for x in range(1000, 101, -1):
        for y in range(1000, 101, -1):
            z: int = x * y
            z_str = str(z)
            if z_str == z_str[::-1] and z > max_palindrom:
                max_palindrom = z
    return max_palindrom


print(compare_digits())
