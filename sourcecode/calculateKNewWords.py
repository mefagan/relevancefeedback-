import os
import operator
from calculateDocScore import calculateDocScore
from getWordsForScoring import getWordsForScoring
def calcNewQuery(k, q, rqSize):

  uniqueWordsSansQuery = getWordsForScoring(q)
  print(" k = ")
  print(k)
  i = 0
  d = {}
  path = 'noStopWords_files'
  words = ["hey", "hi", "wikipedia", "test", "math", "like", "liquid", "geological"]
  for word in words:
  #for word in uniqueWordsSansQuery:
    score = 0
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as myfile:
          
          text = myfile.read()
          if word in text:
            score = score + calculateDocScore(text, word, q, rqSize)
    print(word)
    print(score)
    d[word] = score
  sorted_d = sorted(d.items(), key=operator.itemgetter(1))
  print("length of list")
  print(len(sorted_d))
  end = len(sorted_d)-1
  new_words = []
  m = 0
  while m < int(k):
    x = sorted_d[end]
    print("here")
    print x[0], x[1]
    new_words.append(x[0])
    end = end - 1
    m = m+1
  queryWords = q.split()
  for word in new_words:
    queryWords.append(word)
  newQuery = ' '.join(queryWords)
  print("newQuery is ")
  print(newQuery)
  return newQuery

