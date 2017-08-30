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


def getFormattedDate():
	zone =  timezone('EST')
	dateOnly = datetime.now(zone).strftime('%Y.%m.%d')
	print('---------',dateOnly,'---------')
	return dateOnly

print(getFormattedDate().strftime('%m-%d-%y'))