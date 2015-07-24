#!/usr/bin/python
import sys
import re
import itertools

#=================================================================================
# FUNCTIONS
#=================================================================================
def GetLetters(letter): 
	Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	i = 0
	for l in Alphabet:
		if l == letter:
			return [Alphabet[i-1], Alphabet[i+1]]
		i += 1

#=================================================================================
# PROCESSING
#=================================================================================

# grab parameters
if len(sys.argv) < 2:
	print 'Usage: LetterReplacement.py "code phrase" '
	print 'Example: LetterReplacement.py "" '
	exit()

CodePhrase = sys.argv[1].lower()
print "CodePhrase: "
print CodePhrase
print ""

# Load Dictionary files...
# Load Dictionary
print "Loading Dictionary... "
SortedWords = {}
Dictionary = {}
fp = open("words.txt", "r")
for FileRow in fp:
	Word = FileRow.strip()
	SortedLetters = ''.join(sorted(Word))
	if SortedLetters not in SortedWords:
		SortedWords[SortedLetters] = []
	SortedWords[SortedLetters].append(Word)
	Dictionary[Word]=''

print "Analyzing Phrase... "
# Initialize Lists and Dictionaries
CodeWords = []
for CodeWord in (CodePhrase.split()):
	CodeWords.append(CodeWord)

#Combinations = itertools.combinations(Letters, WordLength)
LetterCombinations = []
for CodeWord in CodeWords:
	NewList = []
	for Letter in CodeWord:
		NewList.append(GetLetters(Letter))
	LetterCombinations.append(NewList)

PossibleWords = []
for i in range(len(CodeWords)):
	CodeWord = CodeWords[i]
	WordLength = len(CodeWord)
	#Generate Indexes for accessing all combinations of the LetterCombinations...
	IndexList = itertools.product(range(2),repeat=WordLength)
	WordList = []
	for Indexes in IndexList:
		PossibleWord = ''
		for j in range(WordLength):
			PossibleWord += LetterCombinations[i][j][Indexes[j]]
		if PossibleWord in Dictionary:
			WordList.append(PossibleWord)
	PossibleWords.append(WordList)

Solutions = itertools.product(*PossibleWords)

for Solution in Solutions:
	Phrase = ""
	for Word in Solution:
		Phrase += Word + " "
	print Phrase


 


