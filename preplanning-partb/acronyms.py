import string
import re

def isAcronym(word):
	
	aF = open("acronyms.txt")
	acronyms = re.split("\n",aF.read())
	
	try:
		acronyms.index(word)
	except:
		if(word.__len__() >= 5):
			return False
		
	return True
	
def getNumAcronyms(row):
	threadID = row[0]
	name = row[2]
	message = row[3]
	
	aF = open("acronyms.txt")
	acronyms = re.split("\n",aF.read())
	
	count = 0
	
	for messageWord in re.split(" ", message):
		formattedWord = messageWord.translate({ord(i): None for i in (string.punctuation+"’…‘")}).lower()
		try:
			acronyms.index(formattedWord)
			count+=1
		except:
			0+0
	
	return count