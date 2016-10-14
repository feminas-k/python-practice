# Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...].
#Write a function cumulative_sum to compute cumulative sum of a list.

def cumulative_sum(l):
	csum = l[:]
	for i in range(1,len(l)):
        	csum[i] = csum[i] + csum[i-1]
	return csum

print cumulative_sum([1,2,3,4])

print cumulative_sum([4,3,2,1])

print cumulative_sum(['a','b','c'])

