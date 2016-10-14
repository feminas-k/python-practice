#Can you make your sum function work for a list of strings as well?

def sum1(liststrings):
	sum2 = ""
	for i in liststrings:
		sum2 = sum2 + i
	return sum2

print sum1(["hello","world"])

print sum1(["aa","bb","cc"])



