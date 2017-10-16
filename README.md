# ExtractFacts

Scrapes daily CNN transcripts, identifies factual claims with the Claimbuster NLP library, and allows people to browse through them with a Django app. 

## Getting Started

To run the scraper/app, you'll need Python 3.x and PostgreSQL 9.5+

### Installing

First, setup a virtual environment and install the required python packages

```
virtualenv env
.\/env/scripts/activate
pip install -r requirements.txt
```

Then create a PostgreSQL database with two tables to store transcript information
```
CREATE TABLE speak (
    claim text,
    speaker text,
    score double precision,
    trans_id text,
    claim_id text NOT NULL,
    date date
);

CREATE TABLE transcript (
    trans_id text NOT NULL,
    script text
);

```
The default database name is practice; the default port is 5432. If either is changed, be sure to replace all instances of "practice" and "5432" in buster.py and settings.py.


## Running the app

To run the scraping script, open up a terminal and enter

```
python buster.py
```

To run the Django webapp locally and explore scored claims in the database, open up a terminal and enter
```
python manage.py runserver
```


## Author

**Asa Royal** 

## Acknowledgments
Thanks to

* Duke Reporter's Lab
* Django Girls