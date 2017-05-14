""" Module SimpleRound contains an example of a simple round used
by playtesters to play sample rounds to train the AI  """

from gameparts import * 
import parse
import random
import csv

NUM_ROUNDS = 3
NUM_NOUNS = 7

class SimpleRound(object):
  
  def __init__(self, nouns, adjs):
    self.nouns = nouns
    self.adjs = adjs
    self.adjsNum = {}
    self.nounsNum = {}
    self.choices = []

  """ Shuffles the deck of nouns in the game"""
  def shuffleNouns(self):
    random.shuffle(self.nouns)

  """ Shuffles the deck of adjectives in the game"""
  def shuffleAdjs(self):
    random.shuffle(self.adjs)

  def shuffleCards(self):
    self.shuffleNouns()
    self.shuffleAdjs()

  def initGame(self):
    for idx in range(len(self.adjs)):
      self.adjsNum[self.adjs[idx].name] = idx + 1
    for idx in range(len(self.nouns)):
      self.nounsNum[self.nouns[idx].name] = idx + 1
    self.shuffleCards()
    print "Hello! Welcome to Priya and Julia's Apples-to-Apples arena!\n"
    name = raw_input("How do we refer to you? ")
    print "Thank you " + name + " for playing our game!\n"
    return name 

  def writeCSV(self):
    output = open('./'+ self.name + '.csv', 'w')
    writer = csv.writer(output)
    writer.writerows(self.choices)

  def playGame(self):
    self.name = self.initGame()

    for i in range(NUM_ROUNDS):
      if i % 30 == 0:
        self.shuffleCards()
      print ("------------------------------------------------\n" + 
        "We will be starting round " + str(i) + " of " + str(NUM_ROUNDS) + " rounds.")
      adj = self.adjs.pop(0)
      nouns = [self.nouns.pop(0) for j in range(NUM_NOUNS)]
      print "This round, you will all be looking for something that is " +  adj.name + "."
      print "Here are your nouns: "
      for noun in range(len(nouns)):
        print str(noun + 1) + ". " + str(nouns[noun])
      judgeChoice = int(raw_input("Choose a card (1-" + str(len(nouns)) + "): ")) - 1

      # save choices into list 
      adjNum = self.adjsNum[adj.name]
      nounNum = self.nounsNum[nouns[judgeChoice].name]
      self.choices.append([adjNum, nounNum])
      print adj.name
      print nouns[judgeChoice].name
      print self.choices

      # add all the adjs/noun cards at the end of their respective decks
      self.adjs.append(adj)
      self.nouns.extend(nouns) 
    
    self.writeCSV()

if __name__ == "__main__":
  nouns = parse.parse_noun_file("trim_nouns.txt")
  adjs = parse.parse_adj_file("trim_adjs.txt") 
  game = SimpleRound(nouns, adjs)
  game.playGame()
