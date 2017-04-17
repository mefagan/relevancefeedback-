#code adapted from http://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python
import sys
import os

def calcGW(word):
	path = 'html_files'
	i = 0
	N = 0
	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as myfile:
			data=myfile.read()
			if (filename!=".DS_Store"):
				N = N +1
			if word in data:
				i = i +1
	return i, N
