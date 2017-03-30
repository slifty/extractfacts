from datetime import datetime
from pytz import timezone
import requests
from bs4 import BeautifulSoup
"""
1. Constantly scrape cnn page looking for new transcripts
2. 
"""
def  timeNow():
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	return dateOnly

def scrapeFeed():
	curPage = requests.get('http://transcripts.cnn.com/TRANSCRIPTS/'+cnnLink())
	print(r.text.encode('utf-8'))
	

cnnLink()


"""
http://transcripts.cnn.com/TRANSCRIPTS/2017.03.21.html
http://transcripts.cnn.com/TRANSCRIPTS/2017.03.25.html

"""