#Write a function lensort to sort a list of strings based on length.

def lensort(l):
	l.sort(key =lambda s :len(s))
        print l


print lensort(['python','perl','java','c','haskell','ruby'])






