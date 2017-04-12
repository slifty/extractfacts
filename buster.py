from bs4 import BeautifulSoup
from datetime import datetime
from difflib import SequenceMatcher
from psycopg2.extras import execute_batch
from pytz import timezone
import psycopg2
import re
import requests
import json

#todo: 
	# 1. change cnnLink() back
	# 2. change scrapeFeed to use findNewTranscripts() again (linksToday array)
	# 3. establish a better primary key for the (speaker,claim,score,transcript_id) database. 
	# 4. create the other database and load
	# 5. create a process to keep this program running (or to check once/day)
	# 6. Clean up the try except in the scrapeFeed() method
	# 7. comment better
	# 8. Instead of running a bunch of execute statements for sequal insertions,  compile all dictionaries from\
	# 	  claim buster into some data structure and run a batch_execute() on them
	# 9. Create a unique id for claim. 
	# 10. Two tables: (claim_id, claim, speaker, score, trans_id) AND (trans_id, show, date, text)
	# 11. Possible new table: show,speaker
	# 12. claim_id should be a hash of speaker, claim to prevent dupes
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
			#print()

	return transcript_ids

#return similarity of phrases
#using SequenceMatcher because it throws out junk and scores whole word matching highly
def similarity(x,y):
	return SequenceMatcher(None,x, y).ratio()
#scrape each transcript
def scrapeFeed():
	dic = {} #maps id to matching set of speakers/statements
	
	linksToday = findNewTranscripts(cnnLink())
	#linksToday =  ['http://transcripts.cnn.com/TRANSCRIPTS/1704/11/cnr.17.html']
	
	for transcript_link in linksToday:

		personStatements = {} #!!!!!!!!
		
		unique_id = transcript_link[39:-5] #url ending
		details = [unique_id] #contains unique id of transcript, show name, date 
		curPage = requests.get(transcript_link).text
		soup = BeautifulSoup(curPage, 'html.parser')
		
		try: 
			soup.prettify()
			print('it prettified')
			
			show = soup.find_all('p',{'class': 'cnnTransStoryHead'})[-1]
			details.append(show)
			details.append(getFormattedDate().replace('.','-'))


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

			details = tuple(details)
			dic[details] = (speakers, speakerChunks)

			
			

			
		except Exception as e:
			print("error with this transcript")
			print(e)
	return dic
	#return speakers, speakerChunks



#(speaker, claim, transcript id) (trnas id, trans text, show information)

def submitClaimbuster(dic):
	busterBase = 'http://idir-server2.uta.edu/claimbuster/API/score/text/'
	busterEnd = '?format=json'
	for transFacts, chunks in dic.items():
		speakers = chunks[0]
		speakerChunks = chunks[1]
		
		for speaker, chunk in zip(speakers, speakerChunks):
			try:
				chunk = chunk.replace('\n', '')
				submissionLink = busterBase+chunk+busterEnd
				jObject = requests.get(submissionLink).text
				#print(jObject)
				jObject = json.loads(jObject)

				for statement in list(jObject.values())[0]:
					statement['claim'] = statement.pop('text')
					statement['speaker'] = speaker
					statement['score'] = round(statement['score'],3)
					statement['trans_id'] = transFacts[0]
					del statement['index']
					#print(statement)
					cur.execute(sqlClaims, statement)
			except Exception as e:
				print('api submission error')
				print(e)
				return;

#scrapeFeed()
submitClaimbuster(scrapeFeed())

conn.commit()
cur.close()

if conn is not None:
	conn.close()
#while(1):
#	doInserts()