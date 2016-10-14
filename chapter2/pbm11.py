#Write a function dups to find all duplicates in the list.

def dups(l):
	dup1 = []
#	i = 0 
	for i in range(len(l)):
		if l[i] in l[i+1:]:
			dup1.append(l[i])
		else:
			 i = i+1
	return dup1


print dups([1,1,2,3,2,4,6,3])




