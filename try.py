from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import psycopg2
import re
import requests
import json

#(speaker, claim, score, transcript id) (trnas id, show name, date)
try:
	conn = psycopg2.connect("dbname = 'practice' user = 'postgres' host = 'localhost' password = 'butt'")
except:
	print("Can't connect to the database")

cur = conn.cursor()

sqlClaims = '''INSERT INTO speak(speaker, score, claim) VALUES (%(speaker)s, %(score)s, %(claim)s)'''
curPage = requests.get('http://idir-server2.uta.edu/claimbuster/API/score/text/Donald Trump is 70 years old. His wife is 49 years old.?format=json').text

practice = {'Donald Trump': 'I am the President of the United States of America', \
			'Melania Trump': 'I am the First Lady of the United States of America',\
			'Barron Trump:': 'What am I?',\
			'Jared Kushner': 'You are nothing. I am everything. Ask Steve Bannon',\
			'Ivanka Trump': 'I\'m a feminist.'}

for k,v in practice.items():
	busterBase = 'http://idir-server2.uta.edu/claimbuster/API/score/text/'
	busterEnd = '?format=json'
	submissionLink = busterBase+v+busterEnd
	jObject = requests.get(submissionLink).text
	jObject = json.loads(jObject)
	
	for statement in list(jObject.values())[0]:
		statement['claim'] = statement.pop('text')
		statement['speaker'] = k
		statement['score'] = round(statement['score'],3)
		del statement['index']
		print(statement)
		#execute_batch(cur,sqlClaims,statement)
		cur.execute(sqlClaims, statement)
	
	#print(k,statement['score'],statement['claim'])
	
#check = {'claim': 'I wish this would work.', 'speaker': 'Asa', 'score': .39}
#cur.execute(sqlClaims,check)
	#print(type(jObject))
	#print(jObject)

#cur.execute('INSERT INTO speak(speaker, score, claim) VALUES(%s,%s,%s)', ('Trump', .846, 'lalalala'))

conn.commit()
cur.close()

if conn is not None:
	conn.close()
"""

transcript = 'http://transcripts.cnn.com/TRANSCRIPTS/1704/11/nday.03.html'
curPage = requests.get(transcript).text
soup = BeautifulSoup(curPage, 'html.parser')
soup.prettify()

butt = soup.find_all('p',{'class': 'cnnTransStoryHead'})[-1]

print(butt.string)
"""

