#Implement unix command grep. The grep command takes a string and a file as arguments
#and prints all lines in the file which contain the specified string.

from sys import argv
script,filename,string=argv

def grep(string,filename):
	f=open(filename).readlines()
	line_sets=[]
	for line in f:
		if string in line:
			line_sets.append(line)
	return '\n'.join(line_sets)

print grep(str(argv[2]),str(argv[1]))



