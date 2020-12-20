import time
import sys


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n <= 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    n = 10000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo2 = time.time()
    factorial_r(n)
    final2 = time.time()
    print(final2 - comienzo2)
