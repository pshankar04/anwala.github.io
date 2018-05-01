import requests
from bs4 import BeautifulSoup as bs4
import os
blogLinks = []

def getFeed(filename):
		try:
			with open("rawFiles/" + filename) as file:
				raw = file.read()
				html = bs4(raw,"html.parser")
				feed_url = html.findAll("link", rel="alternate",type="application/atom+xml")
				blogLink = feed_url[0]['href']
				print("blogLink:",blogLink)
			return blogLink	

		except:
			print("feed_url",feed_url)
			pass
		

if __name__ == "__main__":

	with open("blogListFile.txt") as f:
		for line in f:
			print("Line",line)
			fileName = line.split('--')[0]
			print("File",fileName)
			blog = getFeed(fileName)
			print("Blog:",blog)
			blogLinks.append(blog)

	with open('feeds/feedsList.txt','w') as file:
		for link in blogLinks:
			file.write(str(link))
			file.write("\n")
		
			
			

					