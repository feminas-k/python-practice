#Improve the unique function written in previous problems
#to take an optional key function as argument 
#and use the return value of the key function to check for uniqueness.

def unique(l,key):
	uni1 = []
	for i in l:
		i = key(i)
	if i not in uni1:
		uni1.append(i)
	return uni1

print unique(["python","java","Python","Java"],key = lambda s: s.lower())


