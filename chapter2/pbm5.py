# Write a function factorial to compute factorial of a number.
#Can you use the product function defined in the previous example to compute factorial?

def product(listnumbers):
        pro = 1
        for i in listnumbers:
                pro = pro*i
        return pro
def factorial(n):
	t=[]
	for i in range(n+1):
		t.append(i)
	t=t[1:]
	return product(t)

print factorial(4)

