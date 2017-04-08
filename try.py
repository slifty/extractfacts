from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import psycopg2
import re
import requests


curPage = requests.get('http://idir-server2.uta.edu/claimbuster/API/score/text/text?format=json').text
print(curPage)


for speaker in range(len(speakers)):
				for otherspeaker in speakerSet:
					if similarity(speakers[speaker],otherspeaker) > .5 and len(speakers[speaker]) < len(otherspeaker):
						speakers[speaker] = otherspeaker