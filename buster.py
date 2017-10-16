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
import random
import sys, os

#thought: all caps text b/w parentheses usually worthless... Regex them out?

#connect to local postgres server  
try:
	conn = psycopg2.connect("dbname = 'practice' user = 'postgres' host = 'localhost' password = 'butt'")
except:
	print("Can't connect to the database")

cur = conn.cursor()

sqlClaims = '''INSERT INTO speak(speaker, score, claim,trans_id, claim_id, date) VALUES (%(speaker)s, %(score)s, %(claim)s, %(trans_id)s, %(claim_id)s, %(date)s) ON CONFLICT ON CONSTRAINT speak_pkey DO NOTHING'''
sqlScript = '''INSERT INTO transcript(trans_id, script) VALUES (%(trans_id)s, %(script)s) ON CONFLICT ON CONSTRAINT transcript_pkey DO NOTHING'''


def getFormattedDate():
	"""Returns today's date in CNN URL format (YYYY.MM.DD)"""
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	print('---------',dateOnly,'---------')
	return dateOnly

def cnnLink():
	"""return link to base CNN transcript page corresponding to date"""
	#return 'http://transcripts.cnn.com/TRANSCRIPTS/2017.10.12.html'
	return 'http://transcripts.cnn.com/TRANSCRIPTS/'+getFormattedDate()+'.html'

def findNewTranscripts(mainPageLink):
	"""scan base CNN transcript page to get links to all individual transcript""" 
	transcript_ids = []
	baseLink = 'http://transcripts.cnn.com'
	page = requests.get(mainPageLink).text
	soup = BeautifulSoup(page, 'html.parser')
	soup.prettify()
	for piece in soup.find_all('div', {'class': 'cnnSectBulletItems'}):
		for anchor in piece.find_all('a', href = True):
			transcript_ids.append(baseLink+anchor['href'])
	print(len(transcript_ids), 'transcripts found')
	return transcript_ids

def similarity(x,y):
	"""Find similarity between two strings using seuencematcher. Looks for "longest contiguous matching subsequence" 	"""
	return SequenceMatcher(None,x, y).ratio()

def cleanHtml(soup, details):
	"""Remove some html tags and script transition statements from 'souped' page; extract header details """
	soup.prettify()

	show = soup.find_all('p',{'class': 'cnnTransStoryHead'})
	transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1] 
	tag1 = str(transcript).replace('<br>','\n') #remove annoying html tags in transcript
	tag2 = tag1.replace('<br/>', '\n')
	return tag2

def identifySpeakersStatements(stringscript):
	"""Break transcript up into matching lists of speakers and statements"""
	speakerChunks = []
	speakers = []
	#lastSpeaker = ''
	prevStart = 0
	end = 1

	stringscript = re.sub('SENATOR ','', stringscript)
	stringscript = re.sub(' \(via telephone\)', '', stringscript)
 

	for m in re.finditer('[A-Z].*[A-Z] ?:', stringscript): #search for beginning of speaker chunk (capital letters + colon) 
		temp = m.group(0)
		if ',' in temp:
			temp = temp[:temp.find(',')] 
		if ':' in temp:
			temp = temp[:temp.find(':')]
		if '.' in temp:
			temp = temp[temp.find('.'):]
		if '(' in temp:
			temp = temp[:temp.find('(')]

		speakers.append(temp)
		#lastSpeaker = temp

		if prevStart:
			speakerChunks.append(stringscript[prevStart:m.start()])
		prevStart = m.end()
		end = m.end()

	return speakerChunks, speakers

def refineSpeakers(speakers):
	"""Lop titles off names; match last name references to firstname-lastname referfences"""
	speakerSet = set(speakers)

	for speaker in range(len(speakers)):
		for otherspeaker in speakerSet:
			if ' ' in otherspeaker and similarity(otherspeaker.split(' ')[-1], speakers[speaker]) > .7 and len(otherspeaker) < 25:
				speakers[speaker] = otherspeaker
			elif similarity(speakers[speaker],otherspeaker) > .465 and len(speakers[speaker]) < len(otherspeaker):
				speakers[speaker] = otherspeaker
	return speakers

def scrapeFeed():
	""" Use above methods to find cnn transcripts, scrape them and organize them into usable data"""
	numErrors = 0
	dic = {} #maps a transcript's details to the set of speakers and statements that comprise the transcript
	scriptSet = []
	linksToday = findNewTranscripts(cnnLink())
	
	for transcript_link in linksToday:
		
		unique_id = transcript_link[39:-5] #url ending
		details = [unique_id] #contains unique id of transcript, show name, date 
		curPage = requests.get(transcript_link).text
		soup = BeautifulSoup(curPage, 'html.parser')
		
		try: 
			stringscript = cleanHtml(soup, details)
			brokenText = identifySpeakersStatements(stringscript)
			speakerChunks = brokenText[0]
			speakers = brokenText[1]

			speakerSet = set(speakers)
			speakers = refineSpeakers(speakers)
			details = tuple(details)
			dic[details] = (speakers, speakerChunks)
			scriptSet.append({'trans_id': details[0], 'script' : stringscript})

		except Exception as e:
			numErrors+=1
			print('continuing despite error:', e)

	execute_batch(cur, sqlScript, scriptSet) #store entire transcript in separate table of database
	print(numErrors, 'bad transcripts thrown out.')
	print(len(linksToday) - numErrors, 'transcripts sucessfully processed')
	return dic

def getClaimHash(speaker, claim, trans_id):
	"""Create a hash value from the text of a claim, the claim's speaker, the transcript id(show/date) and a random number. Used as a SQL primary key"""
	hashString = speaker+claim+trans_id+str(random.randint(0,500))
	hashByte = hashString.encode('utf-8')
	hash_obj = hashlib.md5(hashByte)
	return hash_obj.hexdigest()

listem = [] #list of all claimbuster responses

def submitClaimbuster(dic):
	"""Submit chunks of text to the Claimbuster API for scoring. """
	print('Submitting claims to Claimbuster')
	numErrors = 0
	numClaims = 0
	busterBase = 'http://idir-server2.uta.edu:80/factchecker/score_text/'
	busterEnd = '?format=json'
	td = getFormattedDate().replace('.','-')
	for transFacts, chunks in dic.items(): 
		speakers = chunks[0]
		speakerChunks = chunks[1]
		
		for speaker, chunk in zip(speakers, speakerChunks):
			try:
				chunk = chunk.replace('\n', '')
				submissionLink = busterBase+chunk+busterEnd
				jObject = requests.get(submissionLink).json() #submit each chunk of text in each transcript to claimbuster

				for statement in jObject['results']:
					insert = {}
					insert['speaker'] = speaker
					insert['score'] = round(statement['score'],3)
					insert['trans_id'] = transFacts[0]
					insert['claim'] = statement['text'].replace('+', ' ')
					insert['claim_id'] = getClaimHash(speaker, statement['text'], transFacts[0])
					insert['date'] = td
					
					numClaims+=1
					listem.append(insert)
					if numClaims%100 == 0: 
						print(numClaims,'claims processed')

			except Exception as e:
				print('error',e)
				numErrors+=1

	print("API submission errors:", numErrors)

def insertDatabase():
	"""Insert scored claims into postgres database""" 
	execute_batch(cur, sqlClaims, listem)
	conn.commit()
	cur.close()
	if conn is not None:
		conn.close()


x = time.time()
dic = scrapeFeed()
submitClaimbuster(dic)
insertDatabase()
print('elapsed time:', time.time()-x, 'seconds')

