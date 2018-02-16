from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from BeautifulSoup import BeautifulSoup
from requests import Request, Session
import json
import time
import requests


ckey = 'L9QTLPWp2CswcJWRRaNtrsxWO'
csecret = 'nKm7PFmtFAWQYupqffdLz6YWD23VzFlNV8myAei7BaFYDNIoZN'
atoken = '962415725104324608-gJ39MDzaSIlbj44ZBSIuhezb3QcgOAx'
asecret = 'SD9uFFWZH5zfrg4taMdjXkH3vefgmqpPne10EmPiXLijg'
count = 0
uniqueLinks = set([])
linksFile = open("1000TwitterLinks.txt","w")

class listener(StreamListener):
	
	def on_data(self, data):
		global count
		if(count == 1300):
			return False
		else:	
			tweetJson = json.loads(data)
			username = tweetJson['user']['screen_name']
			links = tweetJson['entities']['urls']

			if( len(links) != 0 and tweetJson['truncated'] == False ):
				links = self.getLinksFromTweet(links)
		
				for link in links:
					global uniqueLinks,linksFile
					if(link in uniqueLinks):
						pass
					else:
						print(link)
						count = count + 1
						uniqueLinks.add(link)
						linksFile.write(link)
	     				linksFile.write('\n')	
			# time.sleep(1)				
		return True

	def getLinksFromTweet(self, linksDict):

		links = []
		destUrl = ''
		for uri in linksDict:

			if("https://twitter.com" in uri['expanded_url']):
				pass
			else:
				destUrl = self.checkForRedirection(uri['expanded_url'][0:])
				links.append(destUrl)

		return links

	def checkForRedirection(self,link1):
		response = requests.get(link1, verify=False, timeout=10)
		return response.url
		 	


	def on_error(self, status):
		# print( status )
		if status == 420:
			#returning False in on_data disconnects the stream
			return False
		return True
	
	
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)	
try:
	twitterStream = Stream(auth, listener())		
	twitterStream.filter(track=['football'])
except:
	twitterStream.filter(track=['football'])
			






