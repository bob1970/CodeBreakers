#!/usr/bin/python
import sys

#functions
def IsNumeric(n):
	try:
		float(n)
		return True
	except ValueError:
		return False

#Grab parameters
if len(sys.argv) < 2:
	print 'Usage: AllInaRow.py "a bunch of numbers" '
	print 'Example: AllInaRow.py "187564231587" '
	exit()

#Grab Input Phrase
Numbers = sys.argv[1]
print "Numbers:", Numbers

#Make sure the input is numeric
if not IsNumeric(Numbers):
	print "Error: parameters was not numeric"
	print 'Usage: AllInaRow.py "a bunch of numbers" '
	print 'Example: AllInaRow.py "187564231587" '
	exit()

print "Sequential digits that add up to 15:"
for i in range(len(Numbers)):
	Total = int(Numbers[i])
	DisplayTotal = Numbers[i]
	for j in range(i+1,len(Numbers)):
		Total += int(Numbers[j])
		DisplayTotal += Numbers[j]
		if Total == 15:
			print DisplayTotal
			break
		if Total > 15:
			break





		

