# Provide an implementation for map using list comprehensions.

def square(x): return x*x

def my_map(f,t):
	return [f(x) for x in t]

print my_map(square,range(5))


