from fractions import gcd

def index(keys, values, match):
    return {k: [v for v in values if match(k, v)] for k in keys}

def rational(n, d):
    """Construct a rational number that represents N/D."""
    g = gcd(n, d)
    return [n//g, d//g]

def numer(x):
    """Return the numerator of rational number X."""
    return x[0]

def denom(x):
    """Return the denominator of rational number X."""
    return x[1]

