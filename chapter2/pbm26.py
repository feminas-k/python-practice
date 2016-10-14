#Provide an implementation for filter using list comprehensions.

def even(x): return x%2==0

def my_filter(f,t):
	return [x for x in t if f(x)]

print my_filter(even,range(10))


