import csv
import misspellings
import acronyms
import checkOutput

print("opening file...")

file = open("merged-pythondev-help-concat-group.csv")
csvContent = csv.reader(file)

print("overwriting output...")

outFile = open("output.csv","w")
outFile.write("")
outFile.close()
outFile = open("output.csv","a")
outFile.write("id,misspellings,acronyms,messages,authors")

print("scanning rows...")

i = 0

chatID = 1
chatMisspellings = 0
chatAcronyms = 0
chatCount = 0
chatAuthors = []

for row in csvContent:
	if(row.__len__() != 0 and i != 0):
		if(int(row[0]) != chatID):
			print("===END OF CHAT "+str(chatID)+"===")
			outFile.write("\n"+str(chatID)+","+str(chatMisspellings)+","+str(chatAcronyms)+","+str(chatCount)+","+str(chatAuthors.__len__()))
			chatID = int(row[0])
			chatMisspellings = 0
			chatAcronyms = 0
			chatCount = 0
			chatAuthors = []
			print("===START OF CHAT "+str(chatID)+"===")
			
		chatMisspellings += misspellings.getNumMisspellings(row)
		chatAcronyms += acronyms.getNumAcronyms(row)
		chatCount+=1
		
		if(not(chatAuthors.__contains__(row[2]))):
			chatAuthors.append(row[2])
	
	i+=1

file.close()
outFile.close()

outFile = open("output.csv")
outputCSV = csv.reader(outFile)

i = 0

msCorrect = 0
abCorrect = 0

minChats = -1
maxChats = -1
minAuthors = -1
maxAuthors = -1

chatCount = 0
chatTotal = 0
authorTotal = 0

for outRow in outputCSV:
	if(i != 0):
		if(minChats == -1):
			minChats = int(outRow[3])
		if(maxChats == -1):
			maxChats = int(outRow[3])
		if(minAuthors == -1):
			minAuthors = int(outRow[4])
		if(maxAuthors == -1):
			maxAuthors = int(outRow[4])
			
		if(int(outRow[3]) < minChats):
			minChats = int(outRow[3])
		elif(int(outRow[3]) > maxChats):
			maxChats = int(outRow[3])
			
		if(int(outRow[4]) < minAuthors):
			minAuthors = int(outRow[4])
		elif(int(outRow[4]) > maxAuthors):
			maxAuthors = int(outRow[4])
			
		chatCount+=1
		chatTotal += int(outRow[3])
		authorTotal+=int(outRow[4])
		
	i+=1
	
print("closing file...")

outFile.close()

print("writing stats...")

statsFile = open("stats.txt","w")
statsFile.write("min chats: "+str(minChats)+"\nmax chats: "+str(maxChats)+"\nmin authors: "+str(minAuthors)+"\nmax authors: "+str(maxAuthors)+"\naverage chats: "+str(chatTotal/chatCount)+"\naverage authors: "+str(authorTotal/chatCount))

statsFile.close()
	
print("done!")