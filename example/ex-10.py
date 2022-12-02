# Generators
def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2
        
def a_then_b(a, b):
    yield from a
    yield from b

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substring(s):
    if s:
        yield from prefixes(s)
        yield from substring(s[1:])

def partitions(n, m):
    """Yield partition"""
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield p + " + " + str(m)
        yield from partitions(n, m-1)

