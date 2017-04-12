#code adapted from http://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python
import sys
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def stripStopWords(text, i):
	#print(text)
	stop_words = stopwords.words("english")
	#text = text.decode('unicode_escape').encode('ascii','ignore')
	#tokenized_text = word_tokenize(text)
	#print(tokenized_text)
	clean_text = ' '.join([word for word in text.split() if word not in stop_words])
	print(clean_text)

	#print(clean_text)
	#path = 'noStopWords_files'
	#if not os.path.exists(path):
	#	os.makedirs(path)
	#f = str(i)
	#print(text)

	#with open(os.path.join(path, f), 'wb') as temp_file:
	#	temp_file.write(filtered_words#)

def main():
	path = 'strippedHTML_files'
	i = 0
	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as myfile:
			data=myfile.read()
			stripStopWords(data, i)
			i = i+1
if __name__ == '__main__':
	main()