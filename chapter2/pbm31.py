#Generalize the implementation of csv parser to support any delimiter and comments.

print open('a.txt').read()

def parse(filename,delimiter,comments):
	return [line.strip('\n').split(delimiter) for line in open(filename)
		if line[0]!=comments]

print parse('a.txt','!','#')



