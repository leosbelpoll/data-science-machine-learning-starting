# Fn = Fn-1 + Fn-2
import sys

def fibo(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError as e:
        result = fibo(n-1) + fibo(n-2)
        memo[n] = result
        return result

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    print(fibo(10000))

