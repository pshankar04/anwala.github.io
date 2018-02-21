import subprocess
import math

cmd = "grep -ci 'goals' * > grepOutput.txt"
subprocess.call(cmd, shell=True)
count = 0
matchCount = round(0,4)
corpusCount = round(0,4)
docsWithTerm = round(0,4)
idf = round(0,4)
tf = round(0,4)
tfidf = round(0,4)
totalWordsInFile = round(0,4)
num_words = 0
tfDict = {}

def countWordsInFile(fileName):
	global num_words
	with open(fileName, 'r') as f:
		for line in f:
			words = line.split()
			num_words += len(words)
	return num_words
	
linksFile = open('grepOutput.txt','r')
for line in linksFile:
	line = line.replace('\n', '')
	
	if(':txt' in line):
		matchCount = round(int(line[(line.rfind(':')+1):]),4)
		corpusCount = corpusCount + 1
		if(matchCount >= 1):
			line  = line[0:line.rfind(':')]
			totalWordsInFile = countWordsInFile(line)
			print ('line',line)
			print('Total Words :',totalWordsInFile)
			print ('matchCount',matchCount)
			docsWithTerm = docsWithTerm + 1
			tf = round((matchCount / totalWordsInFile),4)
			if(tf >= 0.0003):
				tfDict[line] = tf
			print('\n')
	else:
		continue	
 		
# idf = round((corpusCount / docsWithTerm),4)

idf = math.log(round((corpusCount / docsWithTerm),4)) / math.log(2)
tfidf = round((tf * idf),4) 

print('TFIDF    TF    IDF    	    URL')
print('-----    --    ---    	    ---')

data = dict()
with open('textURLFile','r') as raw_data:
    for item in raw_data:
        if ':txt' in item:
            key,value = item.split(':txt:', 1)
            data[key]=value
        else:
            pass
 
for key, value in tfDict.items(): 
	 key = key[0:key.rfind(':')]  
	 tfIdfValue = round((float(value) * idf),4)
	 tfValue = value
	 url = data[key]
	 print(str(tfIdfValue)+'   '+str(tfValue)+'   '+str(idf)+'   '+url)
	




 
