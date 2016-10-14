#Write a function array to create an 2-dimensional array. 
#The function should take both dimensions as arguments. 
#Value of each element can be initialized to None:

def array(x,y):
	return [[None]*y for i in range(x)]

print array(2,3)
a=array(3,2)
print a
a[0][0]=5
print a 
