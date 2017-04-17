from __future__ import division
from calczWQ import calczWQ
from calcGW import calcGW

def calculateWordScore(word, rqSize):
	gW, N = calcGW(word)
	zWQ = calczWQ(word)
 	

 	a = zWQ/rqSize
 	b = 2*gW/N
 	
 	yWQ = max(0, a-b)
 	
 	return yWQ