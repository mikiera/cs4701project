''' Module Algo is used to run the algorithm for the AI 
that will be used for the Apples to Apples prediction '''

from sklearn.naive_bayes import MultinomialNB
import numpy as np

""" processCSV takes a csv file, processes the data points inside
and returns them as a 2D list where each entry has [adj, noun] """
def processCSV(filename):
  file = open('./data/'+ filename + '.csv', 'rb')
  reader = csv.reader(file)
  output = []
  for row in reader:
    output.append(row)
  return output 


def classify():
  X = np.random.randint(5, size=(6, 100))
  Y = np.array([1, 2, 3, 4, 5, 6])
  clf = MultinomialNB()
  clf.fit(X, Y)
  clf.predict(X[2])
