#Write a function invertdict to interchange keys and values in a dictionary.
#For simplicity, assume that all values are unique.

def invertdict(d):
	new_d={}
	for i,j in d.items():
		new_d[j]=i
	return new_d

print invertdict({'x': 1, 'y': 2, 'z': 3})


