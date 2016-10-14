# Implement a function product, to compute product of a list of numbers.

def product(listnumbers):
	pro = 1
	for i in listnumbers:
		pro = pro*i
	return pro

print product([1,2,3])


