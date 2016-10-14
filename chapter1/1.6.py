def square(x):
	return x*x

print square(5)

print square(2)+square(3)
print square(square(3))

def sum_of_squares(x,y):
	return square(x)+square(y)

print sum_of_squares(2,3)

#function'square' is passed as argument to other function'f'
f=square
print f(4)

#function 'f' is passed to another function 'fxy'
def fxy(f,x,y):
	return f(x)+f(y)

print fxy(square,2,3)

#scope of variables used in functions 

x=0
y=0
def incr(x):
	y=x+1
	return y
print incr(5)
print x,y


