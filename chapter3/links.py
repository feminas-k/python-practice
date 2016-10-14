# Write a program links.py that takes
# URL of a webpage as argument and
# prints all the URLs linked from that webpage.

import urllib
import re

def links(url):
	response = urllib.urlopen(url)
	content = re.findall(r'http://\w+\s*',response.read())
	for link in content:
		print link

links('http://python.org')	

