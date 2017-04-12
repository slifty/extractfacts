from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import psycopg2
import re
import requests
import json


curPage = requests.get('http://idir-server2.uta.edu/claimbuster/API/score/text/Donald Trump is 70 years old. His wife is 49 years old.?format=json').text
print(curPage)


