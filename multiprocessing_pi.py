import random
import time
import sys
import multiprocessing


def random_values(n):
    p = 0
    g = random.Random()
    x = 0
    y = 0
    for i in range(n):
        x = g.random()
        y = g.random()
        if x**2 + y**2 <= 1:
            p += 1
    return p/n     		

def pi_computing(pool):
    prob = pool.map(random_values, [100] * 500)
    return 4 * (sum(prob) / 500)


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(pi_computing(pool))
    print("Time spent:", time.time() - t0)
else:
    print(__name__)
