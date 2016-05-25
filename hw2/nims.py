# Name:
# Section:
# nims.py

def play_nims(pile, max_stones):
  print"Let's play stones!\n Pile: %r stones\n Max Stones: %r" % (pile, max_stones)
  valid1 = False
  valid2 = False
  while pile >= 1:
    if pile <= 1:
      return "Game Over"
    while valid1 == False :
      one_turn = input("\nPlayer 1. How many stones will you take? (Choose between 1 and %d):\n" % max_stones)
      if (one_turn <= max_stones) and (one_turn >=1):
        pile = pile - one_turn
        valid1 = True
        valid2 = False
        print "There are %s stones remaining." % pile
      else:
        print "That's not a valid option!"
    while valid2 == False:
      two_turn = input("\nPlayer 2. How many stones will you take? (Choose between 1 and %d):\n" % max_stones)
      if (two_turn <= max_stones) and (two_turn >=1):
        pile = pile - two_turn
        valid2 = True
        valid1 = False
        print "There are %s stones remaining." % pile
      else:
        print "That's not a valid option!"

  print "Game over!"
play_nims(100, 10)