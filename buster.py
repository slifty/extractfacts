from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import re
import requests
"""
1. Constantly scrape cnn page looking for new transcripts
2. 
"""
def  timeNow():
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	return dateOnly

def cnnLink():
	return 'http://transcripts.cnn.com/TRANSCRIPTS/'+timeNow()+'.html'

def scrapeFeed():
	#curPage = requests.get(cnnLink())
	personStatements = {}

	curPage = requests.get('http://transcripts.cnn.com/TRANSCRIPTS/1703/31/sn.01.html').text
	soup = BeautifulSoup(str(curPage), 'html.parser')
	soup.prettify()


	transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1]
	stringscript = re.sub('\(.*[A-Z].*[A-Z].*\)', '', str(transcript).replace('<br>','\n')) #remove html tags and transition statements

	print(stringscript)


	
	

#cnnLink()
scrapeFeed()
#while(1):
#	doInserts()


