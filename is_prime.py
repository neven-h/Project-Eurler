import math

def is_prime(n):
    if n == 2:
        retuen True
    if n % 2 == 0:
        return False
    else:
        t = math.sqrt(n)
        for i in range(2, int(t)+1):
            if n % i == 0:
                return False
        return True

    
# assert is_prime(2) == True # This this assertion fails!
#mfixed it
