#!/usr/bin/env python

from optparse import OptionParser
import sys
import random 
import string

def loaddictionary(dictionaryfile="linux.words"):
	dictionary=[]
	ascii= set(string.ascii_lowercase)
	try:
		f = open(dictionaryfile, "r")
	except:
		if dictionaryfile=="linux.words":
			print("The file linux.words was not found; it's usually found in /usr/share/dict/linux.words; copy it into the currect directory")
		else:
			print("The file " + dictionaryfile + " was not found; please verify the file exists.") 
		return []
	prev=""
	for x in f:
		# String out Extra Spaces and New Lines
		temp=x.rstrip().lower()
		if all(y in ascii for y in temp):
			if not prev==temp:
				dictionary.append(temp)
			prev=temp
	return dictionary



def getwords(inputstring, wordlength, dictionarydata):
	letters=[]
	dictionary=[]
	currentstring=inputstring.lower()
	originalstring=inputstring
	words=[]
	for x in inputstring:
		letters.append(x)

	for x in dictionarydata:
		# String out Extra Spaces and New Lines
		temp=x.rstrip()
		# Don't add anything to a dictonary that is too short or too long
		if len(temp)==wordlength:
			dictionary.append(temp)

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
											
'''def anagrams(inputstring, dictonaryfile):
	inputstring=inputstring.lower()
	length=len(inputstring)
	list=[]
	for x in range(length):
		list.append(x)
	random.shuffle(list)
	for x in list:
		words=getwords(options.chars, x, dictionary)
		for y in words:
			temp=inputstring
			temp2=""
			for z in y:
				if not z in temp:
					temp2=z+temp2
						
			print(temp2)
	return []'''	

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-c", "--chars", help="Characters")
	parser.add_option("-l", "--length", type="int", help="Length of Characters")
	parser.add_option("-d", "--dictionary", help="Dictionary File", default="linux.words")
	#parser.add_option("-a", "--anagram", action="store_true", default=False, help="Generate Anagrams (ignores length)")

	(options, args) = parser.parse_args()

	if not options.chars:
		print("Characters are required, see -h")
		exit(1)

	'''if not options.anagram:
		if not options.length:
			print("Length is required, see -h (not required if using anagram)")
			exit(1)'''

	if not options.length:
		print("Length is required, see -h")
		exit(1)


	if not options.dictionary:
		dictionary="linux.words"
	else:
		dictionary=options.dictionary

	'''if options.anagram:
		words=anagrams(options.chars, dictionary)
	else:
		words=getwords(options.chars, int(options.length), dictionary)'''

	dictionarydata=loaddictionary(dictionary)
	words=getwords(options.chars, int(options.length), dictionarydata)

	for x in words:
		print(x)

