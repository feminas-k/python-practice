# Provide an implementation for min and max functions

def minlist(l):
	min1 = l[0]
	for i in l:
		if i < min1:
			min1 = i
	return min1

print minlist([5,3,6,8])



def maxlist(l):
	max1 = l[0]
	for i in l:
		if i > max1:
			max1 = i
	return max1

print maxlist([3,2,5,9,8,4])


