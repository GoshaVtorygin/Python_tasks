import math
import timeit

def is_prime(value):
    sqr = int(math.sqrt(value)) + 1
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    
    i = 3
    while i < sqr:
        if value % i == 0:
            return False
        i += 2
    return True

def is_prime_fermat(value):
    if value == 2:
        return True
    if pow(2, value - 1, value) == 1:
        return True
    return False


print(is_prime(59), timeit.timeit('is_prime(59)', 'from __main__ import is_prime'))
print(is_prime_fermat(59), timeit.timeit('is_prime_fermat(59)', 'from __main__ import is_prime_fermat'))
print(is_prime(2*20-1), timeit.timeit('is_prime(2*20-1)', 'from __main__ import is_prime'))
print(is_prime_fermat(2**20-1), timeit.timeit('is_prime_fermat(2*20-1)', 'from __main__ import is_prime_fermat'))

