import subprocess
from boilerpipe.extract import Extractor
import sys
import hashlib


reload(sys)
sys.setdefaultencoding('utf8')

linksDict = {}
linksFile = open('1000TwitterLinks.txt','r')
for link in linksFile:
	if(link == ''):
		pass
	else:
		try:
			curlCommand = 'curl ' + link
			hash_object = hashlib.md5(link)
			print(hash_object.hexdigest() + '.html')
			htmlFile = hash_object.hexdigest() + ':htmlFile'
			textFile = hash_object.hexdigest() + ':txt'
			f = open(htmlFile, "w")
			raw_html = subprocess.call(curlCommand, shell=True, stdout=f)
			extractor = Extractor(extractor='ArticleExtractor', url=link)
			with open(textFile, 'w') as the_file:
				the_file.write(str(extractor.getText()))
				linksDict[textFile] = link
				print str(extractor.getText())

		except KeyboardInterrupt:
			exit()		
		except:
			pass


with open('textURLFile', 'w') as file:
	for key,value in linksDict.items():
		file.write('%s:%s\n' % (key, value))	
		
		


	

