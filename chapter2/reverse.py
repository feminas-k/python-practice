#Write a program reverse.py to print lines of a file in reverse order

from sys import argv
script,filename = argv

f = reversed(open(filename).readlines())

for i in f:
	print i






