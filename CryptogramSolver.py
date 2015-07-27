#!/usr/bin/python
import sys
import re

#=================================================================================
# FUNCTIONS
#=================================================================================
def CreateWordTemplate(word):
	Letters = list(word)
	Skip = []
	Template = []
	for Letter in Letters:
		if Letter == "'" or Letter == "." or Letter == "&":
			Template.append(Letter)
		else:
			Template.append('*')
	for i in range(len(Letters)):
		for j in range(len(Letters))[i+1:]:
			if j in Skip:
				continue
			if Letters[i] == Letters[j]:
				Template[i] = i+1
				Template[j] = i+1
				Skip.append(j)					
	return ''.join(str(TemplateItem) for TemplateItem in Template)

def PatternMatch(t1, w1, t2, w2):
	for i in range(len(t1)):
		for j in range(len(t2)):
			if (t1[i] == t2[j]) != (w1[i] == w2[j]):
				return False
	return True

#=================================================================================
# PROCESSING
#=================================================================================
# grab parameters
if len(sys.argv) < 2:
	print 'Usage: CryptogramSolver.py "code phrase" '
	print 'Example: CryptogramSolver.py "alvaml bql vd xol qvbs xv ketsvu kold xolc qlbmeyl xoleq vaedevdt bql vdmc vaedevdt" '
	exit()

CodePhrase = sys.argv[1].lower()
print "CodePhrase: "
print CodePhrase
print ""

# Load Dictionary files...
print "Loading Dictionary..."
fp = open("words.txt", "r")
TemplateWords = {}
for FileRow in fp:
	Word = FileRow.strip()
	Word = Word.lower()
	Template = CreateWordTemplate(Word)
	if Template not in TemplateWords:
		TemplateWords[Template] = []
	TemplateWords[Template].append(Word)
print "Analyzing Phrase... "

# Initialize Lists and Dictionaries
CodeWords = []
PossibleWords = {}
for CodeWord in (CodePhrase.split()):
	CodeWords.append(CodeWord)

#==========================================================================================
# Reduce possible letters in each position of each code word... 
# this will help filter later on when combining all possible words together into one solution
#==========================================================================================
SecretCode = {}
for CodeWord in CodeWords:
	#Start lists for each code letter of code phrase...
	for Letter in CodeWord:
		if Letter not in SecretCode:
			SecretCode[Letter] = []

	#Populate lists for each code letter taking care to only record the intersections
	#for letters that repeat more than once in the phrase
	PossibleLetters = {}
	for PossibleWord in TemplateWords[CreateWordTemplate(CodeWord)]:
		for i in range(len(CodeWord)):
			if CodeWord[i] not in PossibleLetters:
				PossibleLetters[CodeWord[i]] = []
			if PossibleWord[i] not in PossibleLetters[CodeWord[i]]:
				PossibleLetters[CodeWord[i]].append(PossibleWord[i])
	for Letter in CodeWord:
		if(len(SecretCode[Letter]) > 0):
			NewList = [val for val in SecretCode[Letter] if val in PossibleLetters[Letter]]
			SecretCode[Letter] = NewList
		else:
			SecretCode[Letter] = PossibleLetters[Letter]

#==============================================================================================
# use reduced letters (SecretCode) to parse together regular expressions to filter out
# words that have been eliminated based on the code phrase and letter analysis
#==============================================================================================
PossibleWords = {}
for CodeWord in CodeWords:
	PossibleWords[CodeWord] = []
	for PossibleWord in TemplateWords[CreateWordTemplate(CodeWord)]:
		#Create RegEx...
		RegEx = ""
		for i in range(len(CodeWord)):
			RegEx += "["
			for Letter in SecretCode[CodeWord[i]]:
				RegEx += Letter
			RegEx += "]"
		#print RegEx, PossibleWord
		Match = re.match(RegEx, PossibleWord)
		if Match:
			#print "getting here..."
			PossibleWords[CodeWord].append(Match.group(0))

#==========================================================================================
# now we have to pattern match the remaining words based on the pattern of the cryptogram... 
# this should further filter down the remaining words drastically.
#==========================================================================================
for i in range(0,len(CodeWords),1):
	for j in range(i+1,len(CodeWords),1):
		CodeWord1 = CodeWords[i]
		CodeWord2 = CodeWords[j]
		if CodeWord1 == CodeWord2: continue
		#print CodeWord1, CodeWord2
		for PossibleWord1 in PossibleWords[CodeWord1][:]:
			MatchFound = False
			for PossibleWord2 in PossibleWords[CodeWord2]:
				if PatternMatch(CodeWord1, PossibleWord1, CodeWord2, PossibleWord2):
					MatchFound = True
			if not MatchFound:
				PossibleWords[CodeWord1].remove(PossibleWord1)
		for PossibleWord2 in PossibleWords[CodeWord2][:]:
			MatchFound = False
			for PossibleWord1 in PossibleWords[CodeWord1]:
				if PatternMatch(CodeWord2, PossibleWord2, CodeWord1, PossibleWord1):
					MatchFound = True
			if not MatchFound:
				PossibleWords[CodeWord2].remove(PossibleWord2)

#==========================================================================================
# Put together possible solutions
#==========================================================================================
LoopCount = 0
CodePhrase = ""
Solutions = []
for CodeWord in CodeWords:
	LoopCount += 1

	if LoopCount == 1:
		CodePhrase = CodeWord
		for PossibleWord in PossibleWords[CodeWord]:
			Solutions.append(PossibleWord)
	else:
		arr = Solutions
		Solutions = []
		for Phrase in arr:
			for PossibleWord in PossibleWords[CodeWord]:
				if PatternMatch(CodePhrase, Phrase, CodeWord, PossibleWord):
					Solutions.append(Phrase + "~" + PossibleWord)
		CodePhrase += "~" + CodeWord 
		#print CodePhrase, "# Solutions: ", len(Solutions)

print ""
print "Possible Solutions: "
print "======================================================================="

# Now just dump the solutions
for Solution in Solutions:
	Phrase = ""
	for Word in Solution.split("~"):
		Phrase += Word + " "
	print Phrase	


