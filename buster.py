from bs4 import BeautifulSoup
from datetime import datetime
from difflib import SequenceMatcher
from psycopg2.extras import execute_batch
from pytz import timezone
import hashlib
import psycopg2
import re
import requests
import json
import time

#todo: 
	
	# 3. establish a better primary key for the (speaker,claim,score,transcript_id) database. 
	# 4. create the other database and load
	# 5. create a process to keep this program running (or to check once/day)
	# 6. Clean up the try except in the scrapeFeed() method
	# 8. Instead of running a bunch of execute statements for sequal insertions,  compile all dictionaries from\
	# 	  claim buster into some data structure and run a batch_execute() on them
	# 9. Create a unique id for claim. Should be a hash of speaker, claim to prevent dupes
	# 10. Two tables: (claim_id, claim, speaker, score, trans_id) AND (trans_id, show, date, text)
	# 11. Possible new table: show,speaker
#todo
"""
#for speaker,chunk in zip(speakers,speakerChunks):
				#print(speaker,chunk)
			#print('-------------------------------')
			# CHANGE CNNLINK METHOD BACK TO HOW IT SHOULD BE
			# Where I am now:
			# If there is at least one word in common between entries in speakers and speakerSet 
			# and its length is >=5, speakers[speaker] = otherspeaker
			# need to end this method by returning speakers, speakerchunks and pass those to another function
			# and that function will interact with the api!
"""


#connect sql 
try:
	conn = psycopg2.connect("dbname = 'practice' user = 'postgres' host = 'localhost' password = 'butt'")
except:
	print("Can't connect to the database")

cur = conn.cursor()

sqlClaims = '''INSERT INTO speak(speaker, score, claim,trans_id) VALUES (%(speaker)s, %(score)s, %(claim)s, %(trans_id)s)'''
#sqlDetails = '''INSERT INTO details('''


#get date in CNN URL format
def getFormattedDate():
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	print('got date')
	return dateOnly


#return today's CNN transcript page URL
def cnnLink():
	print('got link')
	return 'http://transcripts.cnn.com/TRANSCRIPTS/'+getFormattedDate()+'.html'
	
	#return 'http://transcripts.cnn.com/TRANSCRIPTS/2017.05.05.html'

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
			#print()
	print('got transcript urls')
	return transcript_ids

#return similarity of phrases
#using SequenceMatcher because it throws out junk and scores whole word matching highly
def similarity(x,y):
	return SequenceMatcher(None,x, y).ratio()


def cleanHtml(soup, details):
	"""Remove some html tags and script transition statements from 'souped' page; extract header details """
	soup.prettify()
	print('it prettified')

	show = soup.find_all('p',{'class': 'cnnTransStoryHead'})[-1]
	details.append(show)
	details.append(getFormattedDate().replace('.','-'))

	transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1]
	return re.sub('\(.*[A-Z].*[A-Z].*\)', '', str(transcript).replace('<br>','\n')) #remove html tags and transition statements

def identifySpeakersStatements(stringscript):
	#For each chunk of text in the transcript, separate a speaker's name from their speech
	speakerChunks = []
	speakers = []
	lastSpeaker = ''
	prevStart = 0

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
	return speakerChunks, speakers

#scrape each transcript
def scrapeFeed():
	dic = {} #maps id to matching set of speakers/statements
	
	linksToday = findNewTranscripts(cnnLink())
	#linksToday =  ['http://transcripts.cnn.com/TRANSCRIPTS/1704/11/cnr.17.html']
	
	for transcript_link in linksToday:

		#personStatements = {} #!!!!!!!!
		
		unique_id = transcript_link[39:-5] #url ending
		details = [unique_id] #contains unique id of transcript, show name, date 
		curPage = requests.get(transcript_link).text
		soup = BeautifulSoup(curPage, 'html.parser')
		
		try: 
			stringscript = cleanHtml(soup, details)
			#brokenText = identifySpeakersStatements(stringscript)
			#speakerChunks = brokenText[0]
			#speakers = brokenText[1]
			prevStart = 0
			speakerChunks = [] #pieces of text w/speaker name
			speakers = []
			lastSpeaker = ''

			for m in re.finditer('[A-Z].*[A-Z] ?:', stringscript):
				temp = m.group(0)
				if ',' in temp:
					temp = temp[:temp.find(',')]
				if ':' in temp:
					temp = temp[:temp.find(':')]

				speakers.append(temp)
				lastSpeaker = temp

				if prevStart:
					speakerChunks.append(stringscript[prevStart:m.start()].strip())
				prevStart = m.end()
				end = m.end()

			speakerChunks.append(stringscript[end:stringscript.index('<br/></br></br></br>')]) #add last speaker chunk
			speakers.append(lastSpeaker)
			


			speakerSet = set(speakers)
			
			for speaker in range(len(speakers)):
				for otherspeaker in speakerSet:
					if ' ' in otherspeaker and similarity(otherspeaker.split(' ')[-1], speakers[speaker]) > .7 and len(otherspeaker) < 25:
						speakers[speaker] = otherspeaker
					elif similarity(speakers[speaker],otherspeaker) > .465 and len(speakers[speaker]) < len(otherspeaker):
						speakers[speaker] = otherspeaker

			details = tuple(details)
			dic[details] = (speakers, speakerChunks)

		except Exception as e:
			print("error with this transcript")
			print(e)
	return dic


def getClaimHash(speaker, claim, trans_id):
	hashString = speaker+claim+trans_id
	hashByte = hashString.encode('utf-8')
	hash_obj = hashlib.md5(hashByte)
	#print(hash_obj.hexdigest())
	return hash_obj.hexdigest()


def submitClaimbuster(dic):
	count = 0
	#busterBase = 'http://idir-server2.uta.edu/claimbuster/API/score/text/'
	busterBase = 'http://idir-server2.uta.edu:80/factchecker/score_text/'
	busterEnd = '?format=json'
	for transFacts, chunks in dic.items():
		speakers = chunks[0]
		speakerChunks = chunks[1]
		
		for speaker, chunk in zip(speakers, speakerChunks):
			try:
				chunk = chunk.replace('\n', '')
				submissionLink = busterBase+chunk+busterEnd
				jObject = requests.get(submissionLink).json()
				print(type(jObject))


				for statement in jObject['results']:
					insert = {}
					insert['speaker'] = speaker
					insert['score'] = round(statement['score'],3)
					insert['trans_id'] = transFacts[0]
					insert['claim'] = statement['text']
					x = getClaimHash(speaker, statement['text'], transFacts[0])+'a'
					#print(x)
					insert['claim_id'] = x
					
					cur.execute(sqlClaims, insert)
					#should instead build a list of dictionaries and use execute_batch

			except Exception as e:
				print('api submission error')
				print(e)
				count+=1
				print(count)
x = time.time()
dic = scrapeFeed()
print(time.time()-x)
submitClaimbuster(dic)
#submitClaimbuster(scrapeFeed())
#findNewTranscripts(cnnLink())

conn.commit()
cur.close()

if conn is not None:
	conn.close()
#while(1):
#	doInserts()