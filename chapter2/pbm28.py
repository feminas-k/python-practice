#Write a function enumerate that takes a list and returns a list 
#of tuples containing (index,item) for each item in the list.

def enumerate(t):
	return [(t.index(i),i) for i in t]

print enumerate(["a","b","c"])

