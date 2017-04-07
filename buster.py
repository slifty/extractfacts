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

#get transcript_ids (links endings) for each transcipt available
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


#scrape each transcript

def scrapeFeed():
	
	linksToday = findNewTranscripts(cnnLink())
	
	for transcript in linksToday:

		personStatements = {} #!!!!!!!!
		

		curPage = requests.get(transcript).text
		soup = BeautifulSoup(curPage, 'html.parser')
		
		try: #some transcripts raise recursion error with bs4.prettify()
			soup.prettify()
			print('it prettified')
			
			transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1]
			stringscript = re.sub('\(.*[A-Z].*[A-Z].*\)', '', str(transcript).replace('<br>','\n')) #remove html tags and transition statements

			
			prevStart = 0
			speakerIndeces = [] #find indices of speaker names
			speakerChunks = [] #pieces of text w/speaker name
			speakers = []
			lastSpeaker = ''

			for m in re.finditer('[A-Z].*[A-Z] ?:', stringscript):
				#speakerIndeces.append((m.start(), m.end()))
				speakers.append(m.group(0))
				lastSpeaker = m.group(0)

				if prevStart:
					speakerChunks.append(stringscript[prevStart:m.start()])
				prevStart = m.end()
				end = m.end()
			speakerChunks.append(stringscript[end:stringscript.index('<br/></br></br></br>')]) #add last speaker chunk
			speakers.append(lastSpeaker)

			for speaker, chunk in zip(speakers, speakerChunks):
				print(speaker, chunk)


			#Where I am now: getting regex to only match the first name when CNN forgets a line break in a paragraph.
			
		except:
			print("error with this transcript")

scrapeFeed()

#while(1):
#	doInserts()