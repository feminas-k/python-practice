#Write a program center_align.py to center align all lines in the given file.

import sys

def center_align(filename):
	for line in open(filename):
		print line.center(50)

center_align(str(sys.argv[1]))


