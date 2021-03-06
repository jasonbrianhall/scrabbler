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
											
def anagrams(inputstring, dictonarydata, dictionary, minlength=3, depth=0, maxdepth=2, prev=""):
	inputstring=inputstring.lower()
	length=len(inputstring)
	list=[]
	for x in range(length):
		if x>=minlength:
			list.append(x)
	random.shuffle(list)
	for x in list:
		words=getwords(inputstring, x, dictionarydata)
		random.shuffle(words)

		for y in words:
			temp=inputstring
			for z in y:
				temp=temp.replace(z, "", 1)
			words2=getwords(temp, len(temp), dictionarydata)
			for k in words2:
				if prev=="":
					#dictionary.append(y + " " + k)
					print(y + " " + k)
				else:
					#dictionary.append(prev + " " + y + " " + k)
					print(prev + " " + y + " " + k)
			if depth<maxdepth:
				if prev=="":
					anagrams(temp, dictionarydata, dictionary, minlength=minlength, depth=depth+1, maxdepth=maxdepth, prev=y)
				else:
					anagrams(temp, dictionarydata, dictionary, minlength=minlength, depth=depth+1, maxdepth=maxdepth, prev=prev + " " + y)
			#print("word: " + y + " Temp: " + temp + " Inputstring: " + inputstring)
							
	return dictionary
		

if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-c", "--chars", help="Characters")
	parser.add_option("-l", "--length", type="int", help="Length of Characters")
	parser.add_option("-d", "--dictionary", help="Dictionary File", default="linux.words")
	parser.add_option("-a", "--anagram", action="store_true", default=False, help="Generate Anagrams (ignores length)")
	parser.add_option("-D", "--depth", type="int", help="Depth of Anagram Search (default is 3)")
	parser.add_option("-m", "--minlength", type="int", help="Min Length of Anagram Word (default is 3)")
	

	(options, args) = parser.parse_args()

	if not options.chars:
		print("Characters are required, see -h")
		exit(1)

	if not options.anagram:
		if not options.length:
			print("Length is required, see -h (not required if using anagram)")
			exit(1)

	'''if not options.length:
		print("Length is required, see -h")
		exit(1)'''


	if not options.dictionary:
		dictionary="linux.words"
	else:
		dictionary=options.dictionary

	dictionarydata=loaddictionary(dictionary)

	if options.anagram:
		try:
			if options.depth>=0:
				maxdepth=options.depth
			else:
				maxdepth=3
		except:
			maxdepth=3
	
		try:
			if options.minlength>=0:
				minlength=options.minlength
			else:
				minlength=3
		except:
			minlength=3

		words=anagrams(options.chars, dictionarydata, dictionary=[], minlength=minlength, depth=0, maxdepth=maxdepth)
	else:
		words=getwords(options.chars, int(options.length), dictionarydata)

	#words=getwords(options.chars, int(options.length), dictionarydata)

	for x in words:
		print(x)

