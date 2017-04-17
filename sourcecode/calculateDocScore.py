from __future__ import division
import os
import math
from calczWQ import calczWQ
from calculateWordScore import calculateWordScore
from calcGW import calcGW

def calculateDocScore(doc, word, q, rqSize):

	query_words = q.split()
	words = doc.split()
	
	lD = len(words)
	cWD = 0
	mQD = 0
	fWQD = 0

	for i in range(len(words)):
	
		w = words[i]
		if w==word:
			cWD = cWD + 1
			start = max(0, i-5)
			end = min(len(words)-1, i+5)
			j = start
			k = 0
			while (j<end+1):
				for q in query_words:
					if words[j]==q:
						
						k = k+1
				
				j = j+1
			if k>1:
				
				fWQD = fWQD+1
				
				k = 0

		for query in query_words:
			
			if query==w:
				mQD = mQD +1
	
	if mQD == 0:
		return 0
	partone = math.sqrt(fWQD/mQD)
	
	parttwo = math.sqrt(cWD/lD)
	
	yWQ = calculateWordScore(word, rqSize)
	
	if cWD == 0: 	
		sWQD = 0
	else:
		sWQD = partone + yWQ*parttwo
	return sWQD