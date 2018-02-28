import csv
import math
from astropy.table import Table, Column
import numpy as np

friendsDictionary ={}
totalCount = 0
friendCountList = []
finalFriendCount = 0
finalMean = 0
finalMedian = 0
finalStandardDeviation = 0

def computeMean():
	global finalMean
	finalMean = round((totalCount / finalFriendCount),2)
	return finalMean


def computeMedian():
	global finalMedian
	
	mid = 0
	friendCountList.sort(key=int)

	mid = len(friendCountList) / 2
	if(mid == 0):
		finalMedian = friendCountList[mid]
	else:
		mid = mid +1	
		finalMedian = friendCountList[mid]
	return finalMedian



def computeStandardDeviation():
	global finalStandardDeviation
	global finalMean
	stdDeviationSum = 0
	for num in friendCountList:
		stdDeviationSum = stdDeviationSum + ((int(num) - int(finalMean)) *  (int(num) - int(finalMean)))
	# print('stdDeviationSum',stdDeviationSum)	
	finalStandardDeviation = round(math.sqrt(stdDeviationSum / finalFriendCount),2)
	return finalStandardDeviation



with open('acnwala-friendscount.csv') as csvfile:
	totalCount = 0
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		if  "FRIENDCOUNT" in row[1]:
			continue
		else:
			friendCountList.append(row[1])
			totalCount = totalCount + int(row[1])
			finalFriendCount = finalFriendCount + 1
	print (totalCount)

friendCountList.sort(key=int)
for num in friendCountList:
	print num

	
mean = [str(computeMean())]
median = [str(computeMedian())]
stdDeviation = [str(computeStandardDeviation())]
t = Table([mean, median, stdDeviation], names=('Mean', 'Median', 'Standard Deviation'))
print t

# print('Mean' + '---' + 'Median' + '---' + 'Standard Deviation')
# print(str(computeMean())+ '---' +str(computeMedian())+ '---' +str(computeStandardDeviation()))


		 
   

