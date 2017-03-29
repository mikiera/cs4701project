""" Class Adjective represents a adjective card
Attributes:
  name: string, the name of the card 
  desc: string, the description of the card"""

class Adjective(object):
  def __init__(self, n, d): 
    self.name = n 
    self.desc = d 

  def __str__(self):
    return ("Name: " + self.name + "\nDescription: " + self.desc + "\n")
