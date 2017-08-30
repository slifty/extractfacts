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
import sys, os


#todo: 
	# 1. Is it time to switch to mongo...?
	# 5. create a process to keep this program running (or to check once/day)
	# 10. Two tables: (claim_id, claim, speaker, score, trans_id) AND (trans_id, show, date,sdfdsfsdfsdfdsjfl text)


#connect sql 
try:
	conn = psycopg2.connect("dbname = 'practice' user = 'postgres' host = 'localhost' password = 'butt'")
	#print('yeah goteem')
except:
	print("Can't connect to the database")

cur = conn.cursor()
zone =  timezone('EST')

sqlClaims = '''INSERT INTO speak(speaker, score, claim,trans_id, claim_id, date) VALUES (%(speaker)s, %(score)s, %(claim)s, %(trans_id)s, %(claim_id)s, %(date)s) ON CONFLICT ON CONSTRAINT speak_pkey DO NOTHING'''
#sqlDetails = '''INSERT INTO details('''


#get date in CNN URL format
def getFormattedDate():
	#zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	print('---------',dateOnly,'---------')
	return dateOnly


#return today's CNN transcript page URL
def cnnLink():
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
			#print(baseLink+anchor['href'])
			transcript_ids.append(baseLink+anchor['href'])
	print(len(transcript_ids), 'transcripts found')
	#print('got transcript urls')
	return transcript_ids

def similarity(x,y):
	"""Find similarity between two strings using seuencematcher. Looks for "longest contiguous matching subsequence" 	"""
	return SequenceMatcher(None,x, y).ratio()


def cleanHtml(soup, details):
	"""Remove some html tags and script transition statements from 'souped' page; extract header details """
	soup.prettify()

	show = soup.find_all('p',{'class': 'cnnTransStoryHead'}) #CNN labels the show name with this html class


	transcript = soup.find_all('p',{'class': 'cnnBodyText'})[-1] #transcript contained in last element of this class
	tag1 = str(transcript).replace('<br>','\n') #
	tag2 = tag1.replace('<br/>', '\n')
	#print(tag2)
	return tag2

def identifySpeakersStatements(stringscript):
	"""extract speakers and claims from transcripts"""
	speakerChunks = []
	speakers = []
	lastSpeaker = ''
	prevStart = 0
	end = 1

	for m in re.finditer('[A-Z].*[A-Z] ?:', stringscript):
		temp = m.group(0)
		#print(temp)
		if ',' in temp:
			temp = temp[:temp.find(',')]
		if ':' in temp:
			temp = temp[:temp.find(':')]

		speakers.append(temp)
		#print(speakers[-1])
		lastSpeaker = temp

		if prevStart:
			speakerChunks.append(stringscript[prevStart:m.start()])
			#print(speakerChunks[-1])
		prevStart = m.end()
		end = m.end()

	#speakerChunks.append(stringscript[end:stringscript.index('<br/></br></br></br>')]) #add last speaker chunk
	#speakers.append(lastSpeaker)
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

	linksToday = findNewTranscripts(cnnLink())
	#linksToday =  ['http://transcripts.cnn.com/TRANSCRIPTS/1704/11/cnr.17.html']
	
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

		except Exception as e:
			numErrors+=1
			print('continuing despite error:', e)
	print(numErrors, 'bad transcripts thrown out.')
	print(len(linksToday) - numErrors, 'transcripts sucessfully processed')
	return dic


def getClaimHash(speaker, claim, trans_id):
	"""Create a hash value from the text of a claim, the claim's speaker and the transcript id(show/date)"""
	hashString = speaker+claim+trans_id
	hashByte = hashString.encode('utf-8')
	hash_obj = hashlib.md5(hashByte)
	return hash_obj.hexdigest()

listem = []

def submitClaimbuster(dic):
	"""Submit chunks of text to the Claimbuster API for scoring. """
	print('Submitting claims to Claimbuster')
	numErrors = 0
	numClaims = 0
	busterBase = 'http://idir-server2.uta.edu:80/factchecker/score_text/'
	busterEnd = '?format=json'
	for transFacts, chunks in dic.items():
		speakers = chunks[0]
		speakerChunks = chunks[1]
		
		for speaker, chunk in zip(speakers, speakerChunks):
			try:
				chunk = chunk.replace('\n', '')
				#print(chunk)
				submissionLink = busterBase+chunk+busterEnd
				jObject = requests.get(submissionLink).json()
				#print("type", type(jObject))


				for statement in jObject['results']:
					insert = {}
					insert['speaker'] = speaker
					insert['score'] = round(statement['score'],3)
					#print(insert['score'])
					insert['trans_id'] = transFacts[0]
					#print(statement['text'])
					insert['claim'] = statement['text'].replace('+', ' ')
					insert['claim_id'] = getClaimHash(speaker, statement['text'], transFacts[0])
					insert['date'] = datetime.now(zone).strftime('%m/%d/%y')

					
					#cur.execute(sqlClaims, insert)
					numClaims+=1
					listem.append(insert)
					if numClaims%100 == 0: 
						print(numClaims,'claims processed')

			except Exception as e:
				print('continuing despite error:',e)
				numErrors+=1


	print("API submission errors:", numErrors)

def insertDatabase():
	"""Insert scored claims into postgres database""" 
	execute_batch(cur, sqlClaims, listem)
	#reset listem afterwards?
	conn.commit()
	cur.close()
	if conn is not None:
		conn.close()


#if date.time = 2300h, do all of this stuff:

x = time.time()
dic = scrapeFeed()
submitClaimbuster(dic)
insertDatabase()
print('elapsed time:', time.time()-x, 'seconds')

