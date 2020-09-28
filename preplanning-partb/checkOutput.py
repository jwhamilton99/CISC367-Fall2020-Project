import csv

def checkMisspellingOutput(row, index):
	misspellings = int(row[1])
	acronyms = int(row[2])
	
	mGSF = open("goldset-misspellings.csv")
	mGS = csv.reader(mGSF)
	
	gsList = list(mGS)
	gsRow = gsList[index]
	if(int(gsRow[1]) == misspellings):
		return True
	else:
		return False
		
def checkAcronymOutput(row, index):
	misspellings = int(row[1])
	acronyms = int(row[2])
	
	mGSF = open("goldset-abbreviations.csv")
	mGS = csv.reader(mGSF)
	
	gsList = list(mGS)
	gsRow = gsList[index]
	if(int(gsRow[1]) == acronyms):
		return True
	else:
		return False