# Write a program to list all files in the given directory

import os

def dir_list(directory):
	t=os.listdir(directory)
	for filename in t:
		print filename

dir_list('/home/feminas/python practice')

