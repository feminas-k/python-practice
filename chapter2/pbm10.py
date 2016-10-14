#Write a function unique to find all the unique elements of a list.

def unique(l):
	
	i = 0
	while i < len(l):
		if l[i] in l[i + 1:]:
			l.pop(i)
		else:
			i = i + 1
	        	
	return l
print unique([1, 2, 2, 3, 4, 3])

print unique([1,2,3,4,2,4,5])

	
