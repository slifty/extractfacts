from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import psycopg2
import re
import requests


#connect sql 
"""
try:
	try:
		conn = psycopg2.connect("dbname = 'claims' user = 'postgres' host = 'localhost' password = '...'")
	except:
		print("Can't connect to the database")

cur = conn.cursor()

sqlClaims = '''INSERT INTO claims(speaker, claim, transcript_id) VALUES (%(speaker)s, %(claim)s, %(transcript_id)s'''
sql
"""

#get date in CNN URL format
def getFormattedDate():
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	return dateOnly

#return today's CNN transcript page URL
def cnnLink():
	return 'http://transcripts.cnn.com/TRANSCRIPTS/'+getFormattedDate()+'.html'

def findNewTranscripts(mainPageLink):
	transcript_ids = []
	baseLink = 'http://transcripts.cnn.com'
	page = requests.get(mainPageLink).text
	soup = BeautifulSoup(page, 'html.parser')
	soup.prettify()
	for piece in soup.find_all('div', {'class': 'cnnSectBulletItems'}):
		for anchor in piece.find_all('a', href = True):
			print(baseLink+anchor['href'])
			transcript_ids.append(baseLink+anchor['href'])
			print()

	return transcript_ids


#scrape a transcript

def scrapeFeed():
	
	linksToday = findNewTranscripts(cnnLink())
	
	transcript = linksToday[7]

	personStatements = {}
	speakerIndeces = [] 
	indeces = [] #indeces of beginning of new speaker statements
	speakerChunks = []

	curPage = requests.get(transcript).text
	print(curPage)
	print('got to point 1') 
	soup = BeautifulSoup(curPage, 'html.parser')
	print('got to point 2')
	soup.prettify()
	print('it prettified')
	transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1]
	stringscript = re.sub('\(.*[A-Z].*[A-Z].*\)', '', str(transcript).replace('<br>','\n')) #remove html tags and transition statements

	print(stringscript)
	print('--------------------------------------------------------------------------')
	"""
		prevStart = 0
		for m in re.finditer('.*[A-Z].*[A-Z].*?:', stringscript):
			speakerIndeces.append((m.start(), m.end()))
			indeces.append(m.end())
			if prevStart:
				speakerChunks.append(stringscript[prevStart:m.start()])
			prevStart = m.start()

		for indices, chunk in zip(speakerIndeces, speakerChunks):
			print(indices, chunk.encode('utf-8'))
		
		"""

scrapeFeed()
#while(1):
#	doInserts()