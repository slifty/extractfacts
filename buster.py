from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import psycopg2
import re
import requests

try:
	try:
		conn = psycopg2.connect("dbname = 'claims' user = 'postgres' host = 'localhost' password = '...'")
	except:
		print("Can't connect to the database")

cur = conn.cursor()

sqlClaims = '''INSERT INTO claims(speaker, claim, transcript_id) VALUES (%(speaker)s, %(claim)s, %(transcript_id)s'''
sql


#get date in CNN URL format
def getFormattedDate():
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	return dateOnly

#return today's CNN transcript page URL
def cnnLink():
	return 'http://transcripts.cnn.com/TRANSCRIPTS/'+getFormattedDate()+'.html'

def findNewTranscripts(mainPageLink):
	return 'http://transcripts.cnn.com/TRANSCRIPTS/......'


#scrape a transcript
def scrapeFeed():
	#curPage = requests.get(cnnLink())
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

	#for index in range(len(indices)):
		#speakerChunks.add(stringscript)	

	#print(stringscript)


	
	

#cnnLink()
scrapeFeed()
#while(1):
#	doInserts()


