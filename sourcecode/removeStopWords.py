#code adapted from http://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python

from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")

def stripStopWords(text):
	text = ' '.join([word for word in text.split() if word not in cachedStopWords])
	return text