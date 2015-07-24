#!/usr/bin/python
import sys
import itertools

# grab parameters
if len(sys.argv) < 2:
	print 'Usage: WordCracker.py "letters" '
	print 'Example: WordCracker.py "yhetlcnrxplj" '
	exit()

Letters = sys.argv[1].lower()

# Load Dictionary
SortedWords = {}
fp = open("words.txt", "r")
for FileRow in fp:
	Word = FileRow.strip()
	SortedLetters = ''.join(sorted(Word))
	if SortedLetters not in SortedWords:
		SortedWords[SortedLetters] = []
	SortedWords[SortedLetters].append(Word)

#=================================================================================
# for all word lengths possible, get all the combinations of letters
# and look for words in the dictionary using those letters
#=================================================================================
for WordLength in range(len(Letters), 2, -1):
	WordList = []
	Combinations = itertools.combinations(Letters, WordLength)
	for Combo in Combinations:
		SortedLetters = "".join(sorted(Combo))
		if SortedLetters in SortedWords:
			for Word in SortedWords[SortedLetters]:
				if Word not in WordList:
					WordList.append(Word)
	FirstTime = True
	for Word in sorted(WordList):
		if FirstTime:
			print "========================================================================"
			print " ", str(WordLength), " letter words:"
			print "========================================================================"
		print Word
		FirstTime = False

