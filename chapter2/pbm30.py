#Write a python function parse_csv to parse csv (comma separated values) files.

print open('a.csv').read()

def parse_csv(filename):
	return [(line.strip('\n')).split(',') for line in open(filename)]

print parse_csv('a.csv')




