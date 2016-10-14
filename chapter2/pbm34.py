#program to print the words in the descending order of the number of occurrences.

def word_frequency(words):
	frequency = {}
	for w in words:
		frequency[w]=frequency.get(w,0)+1
	return frequency

def read_words(filename):
	return open(filename).read().split()

def main(filename):
	frequency = word_frequency(read_words(filename))
	freq = [(word,count) for word,count in frequency.items()]
	freq.sort(key=lambda x: x[1], reverse=True)
	for word,count in freq:
		print word,count

if __name__=='__main__':
	import sys
	main(sys.argv[1])

