def factorial(n):
    """ Calcula el factorial de n
        param n int > 0
        returns n!
    """

    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(-23))
