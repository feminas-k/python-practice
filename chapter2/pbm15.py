#Reimplement the unique function using sets.

def unique(l):
	uni1 = set(l)
	new_l = list(uni1)
	return new_l


print unique([0,1,0,2,3,2,3,4,4,5,6,7])


