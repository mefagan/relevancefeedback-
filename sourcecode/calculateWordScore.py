from calczWQ import calczWQ
from calcGW import calcGW
def calculateWordScore(word):
	gW = calcGW(word)
	zWQ = calczWQ(word)
 	print("g(W) = ")
 	print(gW)
 	print("z(W, Q) = ")
 	print(zWQ)