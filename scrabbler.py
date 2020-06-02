#!/usr/bin/env python

import sys

def main():
	letters=[]
	dictionary=[]
	if len(sys.argv)>2:
		currentstring=sys.argv[1].lower()
		originalstring=sys.argv[1]
		for x in sys.argv[1]:
			letters.append(x)
		# Length of the word being tested
		wordlength=int(sys.argv[2])
	else:
		print("Not enough arguments; requires characters and word length")
		exit(1)
	try:
		f = open("linux.words", "r")
	except:
		print("The file linux.words is not found; it's usually found in /usr/share/dict/linux.words; copy it into the currect directory")
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
			print(word)
											
				
	

if __name__ == "__main__":
	main()

