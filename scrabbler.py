#!/usr/bin/env python
from optparse import OptionParser

import sys

def getwords(inputstring, wordlength, dictionaryfile="linux.words"):
	letters=[]
	dictionary=[]
	currentstring=inputstring.lower()
	originalstring=inputstring
	words=[]
	for x in inputstring:
		letters.append(x)
	
	try:
		f = open(dictionaryfile, "r")
	except:
		if dicontaryfile=="linux.words":
			print("The file linux.words was not found; it's usually found in /usr/share/dict/linux.words; copy it into the currect directory")
		else:
			print("The file " + dictionaryfile + " was not found; please verify the file exists.") 
		exit(1)
	for x in f:
		# String out Extra Spaces and New Lines
		temp=x.rstrip()
		# Don't add anything to a dictonary that is too short or too long
		if len(temp)==wordlength:
			dictionary.append(temp)
	f.close()

	for word in dictionary:
		# Make case insensitive
		temp=word.lower()
		passed=1
		for x in temp:
			if not x in currentstring:
				passed=0
				break
		if passed==1:
			for x in temp:
				counter=temp.count(x)
				counter2=currentstring.count(x)
				if not counter<=counter2:
					passed=0
					break
		if passed==1:
			for x in range(0,wordlength):
				if originalstring[x].isupper():
					if not originalstring[x].lower()==temp[x]:
						passed=0
		if passed==1:
			words.append(word)
	return words
											
				
	

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-c", "--chars", help="Characters")
	parser.add_option("-l", "--length", help="Length of Characters")
	parser.add_option("-d", "--dictionary", help="Dictionary File")


	(options, args) = parser.parse_args()

	if not options.chars:
		print("Characters are required, see -h")
		exit(1)

	if not options.length:
		print("Length is required, see -h")
		exit(1)

	if options.dictionary:
		words=getwords(options.chars, int(options.length), options.dictionary)
	else:
		words=getwords(options.chars, int(options.length))

	for x in words:
		print(x)

