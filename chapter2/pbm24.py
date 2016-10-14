#Provide an implementation for zip function using list comprehensions

def my_zip(t1,t2):
	return [(i,j) for i in t1 for j in t2 if t1.index(i)==t2.index(j)]

print my_zip([1,2,3],['a','b','c'])
print my_zip([1,2,3],['a','b','c','d'])


