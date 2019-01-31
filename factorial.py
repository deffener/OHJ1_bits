def factorial(n):
    ''' A simple function to calculate factorials

    Usable in cases that import math fails for any reason.
    Raises ValueError if called for negative integers.
    Raises TypeError if n is not an int.

    :param n: int, value to calculate factorial for
    :return: int, value of the factorial.
    '''
    if not isinstance(n, int): # we want int.
        raise TypeError('Factorial can only be calculated for integers.')
    elif n < 0: # a positive int!
        raise ValueError('Factorial is not defined for negative values.')
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
