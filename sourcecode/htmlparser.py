from tidylib import tidy_document

def parsehtml(data):
	document, errors = tidy_document(data, options={'numeric-entities':1})
	return document, errors
