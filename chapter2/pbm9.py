#Write a function cumulative_product
#to compute cumulative product of a list of numbers.

def cumulative_product(l):
	cpdt = l[:]
	for i in range(1,len(l)):
		cpdt[i] = cpdt[i] * cpdt[i-1]
	return cpdt

print cumulative_product([1,2,3,4])

print cumulative_product([4,3,2,1])


