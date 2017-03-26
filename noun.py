""" Class Noun represents a Noun object card
Attributes:
  name: string, the name of the card 
  desc: string, the description of the card
  packs: list of strings, the packs that the card belongs to"""

class Noun(object):
  def __init__(self, n, d, p): 
    self.name = n 
    self.desc = d 
    self.packs = p 

  def __str__(self):
    return ("Name: " + self.name + "\nDescription: " + self.desc + "\nPacks: " 
      + str(self.packs))