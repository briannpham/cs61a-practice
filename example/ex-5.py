def split(n):
    return n // 10, n % 10

def sum_digits(n, digit_sum=0):
    """Return the sum of the digits of positive integer n"""
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits(n, digit_sum + last)

def fact(n, result=1):
    if n == 0:
        return result
    return fact(n - 1, result * n)

# Mutual Recursion
# The Luhn Algorithm
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

