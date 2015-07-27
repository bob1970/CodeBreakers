#!/usr/bin/python
import sys
import random

#Grab parameters
if len(sys.argv) < 2:
	print 'Usage: CryptogramCreator.py "code phrase" '
	print 'Example: CryptogramCreator.py "" '
	exit()

#Grab Input Phrase
CodePhrase = sys.argv[1].lower()
print "CodePhrase: "
print CodePhrase
print ""

#Create Cipher
Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabet2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Cipher = {}

random.seed()
for Letter in Alphabet:
	RandomLetter = random.choice(Alphabet2)
	while Letter == RandomLetter:
		RandomLetter = random.choice(Alphabet2)
	Alphabet2.remove(RandomLetter)
	Cipher[Letter] = RandomLetter

#Create Cipher Phrase
CipherPhrase = ""
for c in CodePhrase:
	if c not in Cipher:
		CipherPhrase += c
	else:
		CipherPhrase += Cipher[c]

print CipherPhrase

