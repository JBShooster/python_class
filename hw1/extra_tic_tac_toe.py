print "********** EXTRA **********\n... I got a bit carried away and wanted to manipulate tic-tac-toe more\n"
#This is how we make use of what we have above
print"Welcome to Tic-Tac-Toe!\n"
board = """
         %s | %s | %s
        ------------
         %s | %s | %s
        ------------
         %s | %s | %s
"""
boxes = ["-","-","-","-","-","-","-","-","-"]
possible_choices = [1,2,3,4,5,6,7,8,9]

print "We use raw_input for the player names as they are string\n"
player1 = raw_input("Player1 name: ")
print "Hello, " + player1, "\n"
player2 = raw_input("Player2 name: ")
print "Hello, " + player2, "\n"

print "We use 'input' for choice as these are integers\n"
# def player1_turn

# Where we keep track of score
player1_choices = []
player2_choices = []
turns = 9

def player_turn(choices, player):
  valid = False
  while valid == False:
    try:
      choice = input(player + ", choose between 1 and 9 (and not one that has already been picked):\n")
      if choice not in possible_choices:
        print "That isn't a valid option"
      elif player == player1:
        boxes[choice - 1] = "x"
        choices.append(choice)
        print "You chose ", choice
        print board % tuple(boxes)
        possible_choices.remove(choice)
        valid = True
      elif player == player2:
        boxes[choice - 1] = "o"
        choices.append(choice)
        print "You chose ", choice
        print board % tuple(boxes)
        possible_choices.remove(choice)
        valid = True
    except(NameError, ValueError, TypeError, SyntaxError):
      print "That's not a valid option"

# This one was tough to figure out! However, I learned subset and it changed my life forever.
def find_winner(choices):
  win_combos =[[1,2,3],[1,4,7],[2,5,8],[3,6,9],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]
  for x in win_combos:
    if set(x).issubset(choices):
      return True
  return False

print board % tuple(boxes)
while turns != 0:
  if find_winner(player1_choices):
    print "%s wins! Game Over!" % player1
    break
  elif find_winner(player2_choices):
    print "%s wins! Game Over!" % player2
    break
  elif turns % 2 == 1:
    player_turn(player1_choices, player1)
    turns = turns - 1
    find_winner(player1_choices)
  elif turns % 2 == 0:
    player_turn(player2_choices, player2)
    turns = turns - 1
    find_winner(player2_choices)

if turns == 0:
  print "Nobody wins. :-("