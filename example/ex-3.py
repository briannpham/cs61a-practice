"""Generalization"""

def make_adder(n):
	"""Return a function that takes one argument
	K and return K + N
	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	def adder(k):
		return k + n
	return adder

def apply_twice(f, x):
	return f(f(x))

def square(x):
	return x * x

def triple(x):
	return 3 * x

def compose1(f, g):
	def h(x):
		return f(g(x))
	return h

def curry2(f):
	def g(x):
		def h(y):
			return f(x, y)
		return h
	return g

curry3 = lambda f: lambda x: lambda y: f(x, y)