''' Module Algo is used to run the algorithm for the AI 
that will be used for the Apples to Apples prediction '''

from sklearn.naive_bayes import MultinomialNB
import numpy as np
import csv
import math 

""" processCSV takes a csv file, processes the data points inside
and returns them as a 2D list where each entry has [adj, noun] """
def processCSV(filename, startLine):
  file = open(filename, 'rU')
  reader = csv.reader(file, dialect=csv.excel_tab)
  output = []
  count = 0 
  for row in reader:
    if count >= startLine:
      newRow = row[0].split(',')
      for el in range(len(newRow)):
        newRow[el] = int(newRow[el])
      output.append(newRow)
    count += 1
  return output 


""" runNaiveBayes runs the Naive Bayes algorithm on a the data
points for a single person with name username  """
def runNaiveBayes(username):
  nouns = processCSV("NounClassification.csv", 1)
  data = processCSV("./data/" + username + ".csv", 0)
  X = np.zeros((len(data), len(nouns[0])))
  Y = np.zeros((len(data)))

  # datapt = [adj, noun]
  for idx in range(len(data)): 
    x = nouns[data[idx][1]-1]
    X[idx, :] = np.array(x)
    Y[idx] = data[idx][0]

  # X = np.random.randint(5, size=(6, 100))
  # Y = np.array([1, 2, 3, 4, 5, 6])

  clf = MultinomialNB()
  clf.fit(X, Y)
  return clf


""" classify classifies set of data based of a given model"""
def classify(model, data):
  return model.predict_proba(data)


def getTestData(username):
  nouns = processCSV("NounClassification.csv", 1)
  data = processCSV("./data/" + username + "-test.csv", 0)
  test = []
  for datapt in data:
    # [adj, noun1, noun2, ...]
    test.append(datapt)
  return test


""" getVectors returns the noun vectors for ONE round 
lst is of the form [adj, noun1, noun2, ...] """
def getVectors(lst):
  nouns = processCSV("NounClassification.csv", 1)
  noun_vecs = []
  for idx in range(1, len(lst)):
    noun_vecs.append(nouns[lst[idx]-1])
  return noun_vecs


def getRanking(prob, adj):
  sorted_idx = np.argsort(prob, axis=0)
  print sorted_idx
  return sorted_idx[:, adj]


def performance(user, ai):
  w0 = 0.3
  w1 = 0.2
  w2 = 0.1
  score = 0
  for i in range(len(user)):
    weight = 0.1
    difference = math.abs(user[i]-ai[i])
    if i == 0:
      weight = 0.3
    elif i == 1:
      weight = 0.2
    score += weight*difference
  return score


def run(user):
  model = runNaiveBayes(user)
  testData = getTestData(user) 
  userRanks = processCSV(user + '-ranks.csv', 0)
  for round in testData:
    samples = getVectors(round)
    prob = model.predict_proba(samples)
    adj = round[0]
    aiRanks = getRanking(prob, adj)
    for i in range(len(aiRanks)):
      aiRanks[i] = round[i + 1]
    # compare the ai against user rankings 


if __name__ == "__main__":
  print "haha"
