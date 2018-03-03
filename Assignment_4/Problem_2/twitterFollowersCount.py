import tweepy
import time
import csv
import math
from astropy.table import Table, Column
import numpy as np
#insert your Twitter keys here

ckey = 'L9QTLPWp2CswcJWRRaNtrsxWO'
csecret = 'nKm7PFmtFAWQYupqffdLz6YWD23VzFlNV8myAei7BaFYDNIoZN'
atoken = '962415725104324608-gJ39MDzaSIlbj44ZBSIuhezb3QcgOAx'
asecret = 'SD9uFFWZH5zfrg4taMdjXkH3vefgmqpPne10EmPiXLijg'
totalCount = 0
listDict = {}
twitter_handle='acnwala'
finalMean = 0
finalMedian = 0
finalStandardDeviation = 0
friendCountList = []
count = 1
finalFriendCount = 0


def computeMean():
    global finalMean
    finalMean = round((finalFriendCount / totalCount),2)
    return finalMean


def computeMedian():
    global finalMedian
    
    mid = 0
    friendCountList.sort(key=int)

    avg = len(friendCountList) % 2
    if(avg == 0):
        mid = len(friendCountList) / 2
        finalMedian = friendCountList[mid]
    else:
        mid = len(friendCountList) / 2
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
    finalStandardDeviation = round(math.sqrt(stdDeviationSum / totalCount),2)
    return finalStandardDeviation


auth = tweepy.auth.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth,wait_on_rate_limit=True)

if(api.verify_credentials):
    print 'Logged in successfully'

for follower in tweepy.Cursor(api.followers, screen_name=twitter_handle).items(): 
    totalCount = totalCount + 1
    listDict[follower.screen_name] = follower.friends_count
    friendCountList.append(follower.friends_count)

friendCountList.sort(key=int)
f = open('twitterFollwers-Friends.txt','w')
for friendCount in friendCountList:
    f.write(str(count)+","+str(friendCount))
    f.write('\n')
    count = count + 1
    finalFriendCount = finalFriendCount + friendCount
f.close()    

mean = [str(computeMean())]
median = [str(computeMedian())]
stdDeviation = [str(computeStandardDeviation())]
t = Table([mean, median, stdDeviation], names=('Mean', 'Median', 'Standard Deviation'))
print t

  
