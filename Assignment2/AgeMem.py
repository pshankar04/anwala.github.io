import requests
import csv
import json
import sys
from datetime import datetime

noAge = 0
noMementos = 0

plotMementosDict = {}
totalURI = 0
f = open('1000TwitterLinks.txt','r')
for link in f:
	if(link == ''):
		pass
	else:
		try:
			totalURI = totalURI + 1
			carbonDateResponse = requests.get("http://cd.cs.odu.edu/cd/"+link)
			mementoResponse = requests.get("http://memgator.cs.odu.edu/timemap/json/"+link,stream=True,headers={'User-Agent': 'Mozilla/5.0'})
			print('Carbon Date status :',carbonDateResponse.status_code)
			print('Mementos status :',mementoResponse.status_code)
			carbonDateResponseJSON = carbonDateResponse.json()
			totalMementos = mementoResponse.headers["X-Memento-Count"]
			ageDate = carbonDateResponseJSON["estimated-creation-date"]

			if(ageDate == ""):
				noAge = noAge + 1
			if(totalMementos == '0'):
				noMementos = noMementos + 1

			print('No mementos: ', noMementos)
			print('No Carbon Date: ', noAge)

			if carbonDateResponse.status_code==200 and mementoResponse.status_code==200:
				print("INSIDE")
				now = datetime.now()
				createdDate = datetime.strptime(ageDate, '%Y-%m-%dT%H:%M:%S')
				currentAge = (now - createdDate)
				print('age: ', currentAge.days)
				print('Memento: ',totalMementos)
				plotMementosDict[str(currentAge.days)] = totalMementos

		except KeyboardInterrupt:
			exit()		
		except:
			print("An exception")
			pass

print('Total URIs',totalURI)
print('No Mementos',noMementos)
print('no date estimate',noAge)

# for age in plotMementosDict:
# 	print(str(age),str(plotMementosDict[age]))

with open('carbonDate.csv', 'wb') as csv_file:
	fieldsnames = ['currentAge','Mementos']
	writer = csv.DictWriter(csvfile, fieldnames=fieldsnames)
	writer.writeheader()
	# writer = csv.writer(csv_file)
	for age, MementoValue in plotMementosDict.items():
		writer.writerow({'currentAge': age, 'Mementos': MementoValue})
		# writer.writerow([age, MementoValue])	
				
			

			
