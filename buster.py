from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import psycopg2
import re
import requests

transcript_ids = []
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
	#transcript_ids = []
	baseLink = 'http://transcripts.cnn.com'
	page = requests.get(mainPageLink).text
	soup = BeautifulSoup(page, 'html.parser')
	soup.prettify()
	for piece in soup.find_all('div', {'class': 'cnnSectBulletItems'}):
		for anchor in piece.find_all('a', href = True):
			print(baseLink+anchor['href'])
			#transcript_ids.append(anchor['href'])
			print()

	return transcript_ids




findNewTranscripts(cnnLink())

#scrape a transcript
"""
def scrapeFeed():
	for transcript in transcript_ids:

		personStatements = {}
		speakerIndeces = [] 
		indeces = [] #indeces of beginning of new speaker statements
		speakerChunks = []

		#future: curPage = requests.get(findNewTranscripts(cnnLink()))
		curPage = requests.get('http://transcripts.cnn.com/TRANSCRIPTS/1703/31/sn.01.html').text 
		soup = BeautifulSoup(str(curPage), 'html.parser')
		soup.prettify()
		transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1]
		stringscript = re.sub('\(.*[A-Z].*[A-Z].*\)', '', str(transcript).replace('<br>','\n')) #remove html tags and transition statements


		prevStart = 0
		for m in re.finditer('.*[A-Z].*[A-Z].*?:', stringscript):
			speakerIndeces.append((m.start(), m.end()))
			indeces.append(m.end())
			if prevStart: speakerChunks.append(stringscript[prevStart:m.start()])
			prevStart = m.start()
			

		for indices, chunk in zip(speakerIndeces, speakerChunks):

"""

	#for index in range(len(indices)):
		#speakerChunks.add(stringscript)	

	#print(stringscript)


	
	


#scrapeFeed()
#while(1):
#	doInserts()