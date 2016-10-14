#Write a program to print each line of a file in reverse order.

from sys import argv
script,filename = argv

f = open(filename).readlines()
for i in f:
	print i[::-1]


