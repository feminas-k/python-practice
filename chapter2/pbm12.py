#Write a function group(list, size) that take a list 
#and splits into smaller lists of given size.

def group(l,size):
	group1 = []
	while size < len(l):
		a = l[:size]
		group1.append(a)
		l = l[size:]
		
	return group1	


print group([0,1,2,3,4,5,6,7,8,9],2)

print group([1,2,3,4,5,6,7,8,9],3)

print group([1,2,3,4,5,6,7,8,9],4)

	
