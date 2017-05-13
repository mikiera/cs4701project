
def trim(filename, newfile):
  f = open(filename)
  write = open(newfile, 'w')
  noun_cards = []
  for line in f:
    if "Basic Set" in line:
      write.write(line)
  write.close()
  f.close()

# trim("nouns.txt", "trim_nouns.txt")
trim("adjs.txt", "trim_adjs.txt")
