# Write a regular expression to validate a phone number.

import re

def phone(num):
	valid = re.match(r'\d\d\d\d\d\d\d\d\d\d',num)
	if valid:
		print 'The given phone number is valid.'
	else:
		print 'The given phone number is invalid'

phone('9876543210')


		
