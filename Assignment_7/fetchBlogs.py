import requests
blogLinks = []

blogLinks.append('http://f-measure.blogspot.com')
blogLinks.append('http://ws-dl.blogspot.com')

def get100BlogLinks():
	while (len(blogLinks) < 105) : 
		try:
			url="http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
			request = requests.get(url)
			url = request.url.strip('?expref=next-blog/')
			if url not in blogLinks:
				blogLinks.append(url)
		except:
			pass
		
	return 	blogLinks

def saveRawHTML(blogs):
	blogsListFile = open('blogListFile.txt','w') 
	i = 0
	for url in blogs:
		request = requests.get(url)
		rawHtmlData = request.content
		file = open('rawFiles/rawHtml%s.html' % str(i+1), 'w')
		file.write(rawHtmlData)
		file.close()
		blogsListFile.write('rawHtml%s.html' % str(i+1)+"--"+url+" \n")
		i = i + 1
					
	
if __name__ == '__main__':	
	print("Length :",str(len(get100BlogLinks())))	
	saveRawHTML(get100BlogLinks())	