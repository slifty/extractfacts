# ExtractFacts

Find factual claims in daily CNN transcripts

## Process

1. Every night, visit CNN's transcript page corresponding to that day's date
2. Follow each link leading to a transcript on the page, and for each transcript:
	* Get rid of html junk
	* Use Regex to find speaker names; break the transcript into chunks based on new speakers
	* Compile two concurrent lists: one of speakers and one of statements those speakers have made in the transcript
	* Use Regex to make sure that speakers in our list are always referred to the same way 
		* e.g. "President Barack Obama", "Barack Obama" and "Obama" should all be recognized as names referring to the same person
	* Link the concurrent lists of speakers and statements to a data structure containing identifying information about the transcript (it's url ending, the name of the show it's from and the date it was created)
	* Insert the above data structure into a larger collection which holds such structures for every transcript uploaded that day
3. For each transcript in the collection:
	* Submit speaker statements to Claimbuster through its API
	* For every claim Claimbuster identifies in the statement, make an insertion to a database with the claim, the transcript_id the claim corresponds to and the speaker of the claim.

## Coming soon

...