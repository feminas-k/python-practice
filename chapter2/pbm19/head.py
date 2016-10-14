#Implement unix command 'head'.
#The head command take a file as argument 
#and prints the first 10 lines of the file.

from sys import argv
script,filename=argv

def head(filename):
	f=open(filename).readlines()
	return ''.join(f[:10])
print head(str(argv[1]))

