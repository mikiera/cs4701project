"""Module Game contains the components for an Apples-to-Apples game:
  Round: records play history of one round
  Game: an instance of an Apples-to-Apples game""" 

from gameparts import * 

# Constants
NUM_CARDS_HAND = 7
NUM_ROUNDS = 5


""" Class Round represents a Round of Apples-to-Apples
  Attributes: 
  - num: int, the round number in the game 
  - adj: Adjective object, the adjective for the round 
  - nouns: list of Noun objects, nouns the judge is choosing between 
  - judge: Player, judge for the round
  - winner: Noun object, the card the judge chose
  - players: list of Players, all players who are not the judge 
  - playerChoices: dictionary mapping player to player's noun choice from hand 
  - playerHands: dictionary mapping player to player's hand for the round"""

class Round(object):

  def __init__(self, num, game, judge, adj):
    self.num = num
    self.adj = adj 
    self.nouns = []
    self.judge = judge
    self.winner = None
    self.players = game.players
    self.playerHands = initPlayerHands(game, judge)
    self.playerChoices = initPlayerChoices(game, judge) 


  def initPlayerHands(game, judge):
    playerHands = []
    for player in game.players:
      if player != judge:
        playerHands[player] = player.hand
    return playerHands


""" Class Game represents an instance of an Apples-to-Apples game
  Attributes;
  - players: list of Player objects 
  - adjs: list of Adjective cards
  - nouns: list of Noun cards"""

class Game(object):

  def __init__(self, nouns, adjs, numPlayers):
    self.nouns = nouns
    self.adjs = adjs
    self.players = initializePlayers(numPlayers)
    self.rounds = []


  """ Initializes the players based on number of players"""
  def initializePlayers(num):
    players = []
    for i in xrange(num):
      name = raw_input("Hello player! What would you like to be called?")
      player = Player(name)
      for i in NUM_CARDS_HAND:  # initialize player hands
        player.append(self.nouns.pop())
      players.append()
    return players


  def playGame():
    for round in NUM_ROUNDS:
      # assign judge
      # execute a round 
      pass