cube = lambda x: x**3
def square(x):
	return x*x

f = square

def fxy(f, x, y):
	 return f(x) + f(y)

print fxy(cube,2,3)

print fxy(lambda x: x**3,2,3)

