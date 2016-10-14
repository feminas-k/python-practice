#Implement unix command 'tail'.
#The tail commands take a file as argument
#and prints the last 10 lines of the file.

from sys import argv
script,filename=argv

def tail(filename):
	f=open(filename).readlines()
	return ''.join(f[-10:])

print tail(str(argv[1]))
