''' Module Algo is used to run the algorithm for the AI 
that will be used for the Apples to Apples prediction '''

from sklearn.naive_bayes import MultinomialNB
import numpy as np

""" processCSV takes a csv file, processes the data points inside
and returns them as a 2D list where each entry has [adj, noun] """
def processCSV(filename, startLine):
  file = open('./data/'+ filename + '.csv', 'rb')
  reader = csv.reader(file)
  output = []
  count = 0 
  for row in reader:
    if count >= startLine:
      output.append(row)
    count += 1
  return output 


""" runNaiveBayes runs the Naive Bayes algorithm on a the data
points for a single person with name username  """
def runNaiveBayes(username):
  nouns = processCSV("noun_features.csv", 1)
  data = processCSV("./data/" + username + ".csv", 0)
  X = np.array((len(data), len(nouns[0])))
  Y = np.array((len(data)))

  # datapt = [adj, noun]
  for idx in range(len(data)): 
    X[idx] = nouns[data[idx][1]-1]
    Y[idx] = data[idx][0]

  # X = np.random.randint(5, size=(6, 100))
  # Y = np.array([1, 2, 3, 4, 5, 6])

  clf = MultinomialNB()
  clf.fit(X, Y)
  return clf


""" classify classifies pieces of data based of a given model"""
def classify(model, data):
  return model.predict(X[2])


if __name__ == "__main__":
  model = runNaiveBayes("cs947")
  X = np.array([])
  result = classify(model, X)
  print result
