from bs4 import BeautifulSoup
from datetime import datetime
from difflib import SequenceMatcher
from pytz import timezone
import psycopg2
import re
import requests
import json


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
	#return 'http://transcripts.cnn.com/TRANSCRIPTS/'+'2017.04.07'+'.html'

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

#return similarity of phrases
#using SequenceMatcher because it throws out junk and scores whole word matching highly
def similarity(x,y):
	return SequenceMatcher(None,x, y).ratio()
#scrape each transcript
def scrapeFeed():
	
	linksToday = findNewTranscripts(cnnLink())
	
	for transcript in linksToday:

		personStatements = {} #!!!!!!!!
		

		curPage = requests.get(transcript).text
		soup = BeautifulSoup(curPage, 'html.parser')
		
		try: 
			soup.prettify()
			print('it prettified')
			
			transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1]
			stringscript = re.sub('\(.*[A-Z].*[A-Z].*\)', '', str(transcript).replace('<br>','\n')) #remove html tags and transition statements

			
			prevStart = 0
			speakerIndeces = [] #find indices of speaker names
			speakerChunks = [] #pieces of text w/speaker name
			speakers = []
			#speakerSet = {}
			lastSpeaker = ''

			#for m in re.finditer('[A-Z].{1,5}[A-Z]?:', stringscript):
			for m in re.finditer('[A-Z].*[A-Z] ?:', stringscript):
				temp = m.group(0)
				if ',' in temp:
					temp = temp[:temp.find(',')]
				if ':' in temp:
					temp = temp[:temp.find(':')]

				speakers.append(temp)
				lastSpeaker = temp

				if prevStart:
					speakerChunks.append(stringscript[prevStart:m.start()])
				prevStart = m.end()
				end = m.end()
			speakerChunks.append(stringscript[end:stringscript.index('<br/></br></br></br>')]) #add last speaker chunk
			speakers.append(lastSpeaker)

			speakerSet = set(speakers)
			
			for speaker in range(len(speakers)):
				for otherspeaker in speakerSet:
					#####HERE IS WHERE POINT 2 SHOULD GO
					#if ' ' in otherspeaker and otherspeaker.split(' ')[-1] == speakers[speaker]:
						#speakers[speaker] = otherspeaker
					if ' ' in otherspeaker and similarity(otherspeaker.split(' ')[-1], speakers[speaker]) > .7 and len(otherspeaker) < 25:
						speakers[speaker] = otherspeaker
					elif similarity(speakers[speaker],otherspeaker) > .465 and len(speakers[speaker]) < len(otherspeaker):
						speakers[speaker] = otherspeaker
			
			#for speaker,chunk in zip(speakers,speakerChunks):
				#print(speaker,chunk)
			print('-------------------------------')
			# CHANGE CNNLINK METHOD BACK TO HOW IT SHOULD BE
			# Where I am now:
			# If there is at least one word in common between entries in speakers and speakerSet 
			# and its length is >=5, speakers[speaker] = otherspeaker
			# need to end this method by returning speakers, speakerchunks and pass those to another function
			# and that function will interact with the api!

			#not all of this method should be within the try except.......
			return speakers, speakerChunks
		except Exception as e:
			print("error with this transcript")
			print(e)

scrapeFeed()

#while(1):
#	doInserts()