"""Module Gameparts contains components for an Apples-to-Apples game
  Noun: card with a noun and description
  Adjective: card with an adjective and description
  Player: a player with a name and hand""" 


""" Class Noun represents a Noun object card
  Attributes:
  - name: string, the name of the card 
  - desc: string, the description of the card
  - packs: list of strings, the packs that the card belongs to"""

class Noun(object):
  def __init__(self, n, d, p): 
    self.name = n 
    self.desc = d 
    self.packs = p 

  def __str__(self):
    return ("Name: " + self.name + "\nDescription: " + self.desc + "\nPacks: " 
      + str(self.packs) + "\n")



""" Class Adjective represents a adjective card
  Attributes:
  - name: string, the name of the card 
  - desc: string, the description of the card"""

class Adjective(object):
  def __init__(self, n, d): 
    self.name = n 
    self.desc = d 

  def __str__(self):
    return ("Name: " + self.name + "\nDescription: " + self.desc + "\n")



""" Class Player represents an instance of a Player
  Attributes:
  - name: string, name of the player
  - hand: list of Noun cards, the player's hand """

class Player(object):
  def __init__(self, name):
    self.name = name
    self.hand = []

  def dealCard(self, card):
    self.hand.append(card)
