# parse.py 
# Parses a text file containing a list of cards

from gameparts import * 

def parse_packs(packstr):
  """Returns a list containing all comma separated pack elements
    packstr: string containing more than one character, may contain commas"""  
  packs = []
  while packstr != "":
    comma = packstr.find(',') 
    if comma == -1:
      packs.append(packstr.strip())
      packstr = ""
    else:
      packs.append(packstr[:comma].strip())
      packstr = packstr[comma+1:]
  return packs


def parse_noun_file(filename):
  """Returns a list of Noun cards 
    filename: name of a list of Nouns (of a specific format)"""
  f = open(filename)
  noun_cards = []
  for line in f:
    hyphen = line.find('-') 
    sqbracket1 = line.find('[')
    sqbracket2 = line.find(']')
    name = line[:hyphen].strip()
    desc = line[hyphen + 1: sqbracket1].strip()
    packs = parse_packs(line[sqbracket1 + 1:sqbracket2].strip())
    n = Noun(name, desc, packs)
    noun_cards.append(n)
  f.close()
  return noun_cards


def parse_adj_file(filename):
  """Returns a list of Adj cards 
    filename: name of a list of Adj (of a specific format)"""
  f = open(filename)
  cards = []
  for line in f:
    colon = line.find(':')
    name = line[:colon].strip()
    desc = line[colon+1:].strip()
    a = Adjective(name, desc)
    cards.append(a)
  f.close()
  return cards