from __future__ import division
import os
from calczWQ import calczWQ
from calcGW import calcGW

def calculateDocScore(doc, word, q):
	print(doc)
	query_words = q.split()
	for pic in query_words:
		print(pic)
	data = doc.read()
	words = data.split()
	lD = len(words)
	print(lD)
	cWD = 0
	mQD = 0
	fWQD = 0


	for i in range(len(words)):
		w = words[i]
		if w==word:
			cWD = cWD + 1
			start = max(0, i-5)
			end = min(len(words)-1, i+5)
			print(end)
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
	print("cWD, which is the number of occurances of random word in doc = ")
	print(cWD)
	print("mQDm which is number of occurances of any query word in doc = ")
	print(mQD)
	print("fWQD = ")
	print(fWQD)