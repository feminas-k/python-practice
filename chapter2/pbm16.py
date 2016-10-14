#Write a function extsort to sort a list of files based on extension.

def exsort(l):
	l.sort(key= lambda x: x.split('.')[1])
	return l


print exsort(['a.c','a.py','b.py','bar.txt','foo.txt','x.c'])


