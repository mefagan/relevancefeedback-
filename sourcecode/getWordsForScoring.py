#http://stackoverflow.com/questions/6181763/converting-a-string-to-a-list-of-words
#http://stackoverflow.com/questions/7794208/how-can-i-remove-duplicate-words-in-a-string-with-python
import os
import re


def getWordsForScoring(query):
	query_words = query.lower().split()
	print("size of query words list")
	print(len(query_words))

	#get a list of all unique words in documents
	ulist = []
	i = 0
	path = 'noStopWords_files'
	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as myfile:
			data=myfile.read()
			l = data.split()
			[ulist.append(x) for x in l if x not in ulist]
			
	print("size of unique words and some random words")
	print(len(ulist))
	print(ulist[134])
	print(ulist[139])
	print(ulist[1340])
	removed_query_words = [x for x in ulist if x not in query_words]
	print(len(removed_query_words))
	print(removed_query_words[134])
	print(removed_query_words[139])
	print(removed_query_words[1340])

	#removed_query_words = ' '.join([word for word in ulist if word not in query_words])
	#print(len(query_words))
	#print(len(removed_query_words))

	#return removed_query_words

def main():
	getWordsForScoring("Wikipedia wikipedia mary hi hello ryan")
if __name__ == '__main__':
	main()