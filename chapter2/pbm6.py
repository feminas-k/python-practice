# Write a function reverse to reverse a list.
# Can you do this without using list slicing?

def reverse(t):
	new=[]
	for i in range(len(t)):
		new.append(t[len(t)-1-i])
	return new

print reverse([1,2,3,4])

print reverse(reverse([1,2,3,4]))


