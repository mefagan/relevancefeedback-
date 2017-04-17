#code adapted from http://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python
import sys
import os

def calcGW(word):
	path = 'html_files'
	i = 0
	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as myfile:
			data=myfile.read()
			if word in data:
				i = i +1
	return i
