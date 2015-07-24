#!/usr/bin/python
import sys

# grab parameters
if len(sys.argv) < 2:
	print 'Usage: JumbleSolver.py "letters letters letters" '
	print 'Example: JumbleSolver.py "" '
	exit()

WordList = sys.argv[1].lower()

# Load Dictionary
SortedWords = {}
fp = open("words.txt", "r")
for FileRow in fp:
	Word = FileRow.strip()
	SortedLetters = ''.join(sorted(Word))
	if SortedLetters not in SortedWords:
		SortedWords[SortedLetters] = []
	SortedWords[SortedLetters].append(Word)

# Process Words
JumbledWords = WordList.split()
for JumbledWord in JumbledWords:
	print "Words for", JumbledWord, ":"
	print "============================================================="
	SortedLetters = ''.join(sorted(JumbledWord))
	for PossibleWord in SortedWords[SortedLetters]:
		print PossibleWord
	print ""

