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
NumberToLetters = {}
NumberToLetters['2'] = ('a','b','c')
NumberToLetters['3'] = ('d','e','f')
NumberToLetters['4'] = ('g','h','i')
NumberToLetters['5'] = ('j','k','l')
NumberToLetters['6'] = ('m','n','o')
NumberToLetters['7'] = ('p','r','s')
NumberToLetters['8'] = ('t','u','v')
NumberToLetters['9'] = ('w','x','y')

# grab parameters
if len(sys.argv) < 2:
	print 'Usage: LetterPlease.py "numeric phrase" '
	print 'Example: LetterPlease.py "" '
	exit()

CodePhrase = sys.argv[1]
print "CodePhrase: "
print CodePhrase
print ""

# Load Dictionary files...
# Load Dictionary
print "Loading Dictionary... "
Dictionary = {}
fp = open("words.txt", "r")
for FileRow in fp:
	Word = FileRow.strip()
	Dictionary[Word]=''

print "Analyzing Phrase... "
# Initialize Lists 
CodeWords = []
for CodeWord in (CodePhrase.split()):
	CodeWords.append(CodeWord)

# Load all letter combinations for all possible words
WordCombinations = []
for NumericCodeWord in CodeWords:
	NewList = []
	for Digit in NumericCodeWord:
		if Digit == ",":
			NewList.append((",",))
			continue
		if Digit in str(range(10)):
			NewList.append(NumberToLetters[Digit])
		else:
			NewList.append((Digit,))
	WordCombinations.append(NewList)


# assemble all letter combinations into possible words and cross reference dictionary and store all valid words	
PossibleWordCombinations = []
for LetterCombinations in WordCombinations:

	Combos = itertools.product(*LetterCombinations)
	NewList = []
	for PossibleWord in Combos:
		if "".join(PossibleWord) in Dictionary:
			NewList.append("".join(PossibleWord))
	PossibleWordCombinations.append(NewList)

# display the solution
# usually too many combinations to dump the whole phrase so it's better to just dump the possible solutions for each
# word and the human mind can quickly figure out the phrase
print ""
print "Word Solutions: "
for i in range(len(CodeWords)):
	PossibleWordList = PossibleWordCombinations[i]
	CodeWord = CodeWords[i]
	WordList = ""
	Comma = ""
	print "" 
	print CodeWord
	for PossibleWord in PossibleWordList:
		WordList += Comma + PossibleWord
		Comma = ", "
	print WordList



