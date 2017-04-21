"""Module Game contains the components for an Apples-to-Apples game:
  Round: records play history of one round
  Game: an instance of an Apples-to-Apples game""" 

from gameparts import * 
import parse
import random
# import kivy

# Constants
NUM_CARDS_HAND = 7
NUM_ROUNDS = 5


""" Class Round represents a Round of Apples-to-Apples
  Attributes: 
  - num: int, the round number in the game (1-indexed)
  - adj: Adjective object, the adjective for the round 
  - nouns: list of Noun objects, nouns the judge is choosing between 
  - players: list of Players, all players who are not the judge 
  - judge: Player, judge for the round
  - winnerCard: Noun object, the card the judge chose
  - winnerPlayer: Player object, the player who chose the winning card 
  - playerChoices: dictionary mapping player to player's noun choice from hand 
  - playerHands: dictionary mapping player to player's hand for the round"""

class Round(object):

  def __init__(self, num, players, judge, adj):
    self.num = num
    self.adj = adj 
    self.nouns = []
    self.players = players
    self.judge = judge
    self.winnerCard = None
    self.winnerPlayer = None
    self.playerHands = {}
    self.playerChoices = {}


""" Class Game represents an instance of an Apples-to-Apples game
  Attributes;
  - players: list of Player objects 
  - adjs: list of Adjective cards
  - nouns: list of Noun cards
  - rounds: list of Round objects, record of the game
  - nextJudge: int, index of the next judge in self.players """

class Game(object):

  def __init__(self, nouns, adjs):
    self.players = []
    self.adjs = adjs
    self.shuffleAdjs()
    self.nouns = nouns
    self.shuffleNouns()
    self.rounds = []
    self.nextJudge = 0
    

  """ Initializes the players based on number of players"""
  def initializePlayers(self, num):
    players = []
    names = []
    for i in xrange(num):
      name = raw_input("Hello player! What would you like to be called?\nName: ")
      while name in names:
        name = raw_input("Sorry that name is taken, what would you like to be called?\nName: ")
      names.append(name)
      ai = raw_input("Are you a human player? (y/n)\nHuman?: ")
      aiBool = True if (ai == 'y') else False 
      player = Player(name, aiBool)
      for i in range(NUM_CARDS_HAND):  # initialize player hands
        player.dealCard(self.nouns.pop())
      players.append(player)
    return players


  """ Initializes the game """
  def initializeGame(self):
    numPlayers = raw_input("Hello! Welcome to Priya and Julia's Apples-to-Apples arena!\n" +
      "How many people will be playing today?\nNumber: ")
    self.players = self.initializePlayers(int(numPlayers))
    print "Very good! Good luck to the " + str(numPlayers) + " of you here today.\n"

  """ Shuffles the deck of nouns in the game"""
  def shuffleNouns(self):
    random.shuffle(self.nouns)

  """ Shuffles the deck of adjectives in the game"""
  def shuffleAdjs(self):
    random.shuffle(self.adjs)

  """ Play a game of Apples to Apples """
  def playGame(self):
    self.initializeGame()
    for r in range(1, len(self.adjs) + 1):     # round are 1-indexed
      # player display info
      print ("------------------------------------------------\n" + 
        "We will be starting round " + str(r) + " of " + str(len(self.adjs)) + " rounds.")

      # assign judge
      judge = self.players[self.nextJudge]
      players = self.players[:]
      players.pop(self.nextJudge)
      self.nextJudge = (self.nextJudge + 1) % len(self.players)
      print "The judge for this round will be " + judge.name + "."

      # choose an adjective 
      adj = self.adjs.pop()
      print "This round, you will all be looking for something that is " +  adj.name + "."

      # start recording info for round
      roundInfo = Round(r, players, judge, adj)
      playerChoices = {}
      nouns = []

      # ask players for their choices 
      for player in players:
        name = player.name
        roundInfo.playerHands[name] = player.hand
        print "------------------------------------------------"
        print ("Hello " + name + "!\nPlease choose a card from 1-" + 
          str(NUM_CARDS_HAND) + " from your hand: ")
        for card in range(len(player.hand)):
          print str(card + 1) + ". " + str(player.hand[card])

        cardNum = int(raw_input("Choose a card: ")) - 1
        card = player.hand.pop(cardNum)
        roundInfo.playerChoices[name] = card
        nouns.append(card)

        newCard = self.nouns.pop()
        player.dealCard(newCard)
        print "You have drawn a new card: " + str(newCard) + "\n"

        # deal used card back into second half of noun deck
        numNouns = len(self.nouns)
        insertIndex = random.randint(numNouns/2, numNouns - 1)
        self.nouns.insert(insertIndex, card)

      # ask the judge to pick a card
      print "------------------------------------------------" * 2 + "\n"
      print ("Hello " + judge.name + ", now it is your turn to choose a card." + 
        "\nAs a reminder, the adjective for this round is: " + str(adj))
      for noun in range(len(nouns)):
        print str(noun + 1) + ". " + str(nouns[noun])
      judgeChoice = int(raw_input("Choose a card (1-" + str(len(nouns)) + "): ")) - 1

      winnerCard = nouns[judgeChoice]
      for player in players:
        if roundInfo.playerChoices[player.name] == winnerCard:
          winnerPlayer = player
      roundInfo.winnerCard = winnerCard
      roundInfo.winnerPlayer = winnerPlayer

      print ("Congratulations to " + winnerPlayer.name + " for choosing the winning"
        + " option: " + winnerCard.name + " for the adjective " + str(adj))


if __name__ == "__main__":
  nouns = parse.parse_noun_file("nouns.txt")
  adjs = parse.parse_adj_file("adjs.txt")
  game = Game(nouns, adjs)
  game.playGame()