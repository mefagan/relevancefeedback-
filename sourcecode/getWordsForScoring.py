#http://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
#http://stackoverflow.com/questions/7794208/how-can-i-remove-duplicate-words-in-a-string-with-python
import os
import re
def getWordsForScoring(query):
	query_words = query.lower().split()

	#get a list of all unique words in documents
	ulist = []
	i = 0
	path = 'noStopWords_files'
	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as myfile:
			data=myfile.read()
			wordList = re.sub("[^\w]", " ",  data).split()
			i = i + len(wordList)
			[ulist.append(x) for x in wordList if x not in ulist]
	print("TESTING STOP LIST")
	print(i)
	print(len(ulist))

		#removed_query_words = ' '.join([word for word in text.split() if word not in stop_words])
def main():
	getWordsForScoring("Wikipedia")
if __name__ == '__main__':
	main()