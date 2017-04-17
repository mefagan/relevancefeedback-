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


	for i in range(len(words)):
		w = words[i]
		if w==word:
			cWD = cWD + 1
		for query in query_words:
			
			if query==w:
				mQD = mQD +1
	print("cWD, which is the number of occurances of random word in doc = ")
	print(cWD)
	print("mQDm which is number of occurances of any query word in doc = ")
	print(mQD)