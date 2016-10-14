#Write a program wrap.py that takes filename and width as aruguments
#and wraps the lines longer than width.

from sys import argv
script,filename,width=argv

def wrap(filename,n):
	for line in open(filename):
		if len(line)>n:
			print line[0:n]
			print line[n:len(line)]
		else:
			print line

wrap(str(argv[1]),int(argv[2]))

