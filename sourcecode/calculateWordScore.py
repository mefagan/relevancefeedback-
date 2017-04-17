from __future__ import division
from calczWQ import calczWQ
from calcGW import calcGW

def calculateWordScore(word, rqSize):
	gW, N = calcGW(word)
	zWQ = calczWQ(word)
 	print("g(W) = ")
 	print(gW)
 	print("z(W, Q) = ")
 	print(zWQ)
 	print("N = ")
 	print(N)

 	a = zWQ/rqSize
 	b = 2*gW/N
 	print("a = ")
 	print(a)
 	print("b = ")
 	print(b)
 	print("a-b")
 	print(a-b)
 	yWQ = max(0, a-b)
 	print("yWQ = ")
 	print(yWQ)
 	return yWQ