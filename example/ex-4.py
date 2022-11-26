from math import sqrt

def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1/n != 0

def remove(n, digit):
    """Return all digits of non-negative N that are not DIGIT,
    for some non-negative DIGIT less than 10
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last * 10**digits
            digits = digits + 1
    return kept

def trace1(fn):
    """Returns a version of fn that first print before it is called
    fn - a function of 1 argument
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x