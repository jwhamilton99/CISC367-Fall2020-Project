import re
import string
import acronyms

def isName(word):
	nF = open("names.txt")
	names = re.split("\n",nF.read())
	
	try:
		names.index(word)
	except:
		return False
		
	return True

def isEmoticon(word):
	w = word.translate({ord(i): None for i in (string.punctuation+"…\n").replace(":","")}).lower()
	if(w.__len__() >= 2):
		if(w[0] == ":" and w[-1:] == ":"):
			return True
	return False
	
def isCode(word):
	w = word.translate({ord(i): None for i in (string.punctuation+"…\n").replace("`","")}).lower()
	if(w.__len__() >= 2):
		if(w[0] == "`" and w[-1:] == "`"):
			return True
	return False
	
def isURL(word):
	if(word.__len__() >= 5):
		if(word[:5] == "https"):
			return True
	return False

def getNumMisspellings(row):
	if(row.__len__() != 0):
		threadID = row[0]
		name = row[2]
		message = row[3]
		
		wF = open("words_alpha.txt")
		words = re.split("\n",wF.read())
		
		count = 0
		
		for messageWord in re.split(" ", message):
			formattedWord = messageWord.translate({ord(i): None for i in (string.punctuation+"’…‘\n”“")}).lower()
			try:
				if(not(acronyms.isAcronym(formattedWord)) and not(isEmoticon(messageWord)) and not(isCode(messageWord)) and not(isURL(formattedWord))):
					if(not(isName(formattedWord))):
						words.index(formattedWord)
			except:
				try:
					int(formattedWord)
				except:
					if(formattedWord != ""):
						print(formattedWord)
						count+=1
			
		return count