#Joel Shooster
#HW 1 - Rock Paper Scissors
#Date: 5/9/2016
#rps.py
print"Welcome to Rock / Paper / Scissors! Such a fun game!\n"

player_one = raw_input("Player 1 name?: ")
print "Welcome, ", player_one, "\n"

player_two = raw_input("Player 2 name?: ")
print "Welcome, ", player_two, "\n"

possible_choices = ['rock', 'paper', 'scissors']
player_index = [1, 2]

def player_choose(player):
  name = ""
  if player == 1:
    name = player_one
  else:
    name = player_two

  choice = raw_input("%s. Rock, paper or scissors?: " % name)
  if choice not in possible_choices:
    print "That isn't a valid option"
    player_choose(player)
  else:
    player_index[player-1] = choice

outcome_p1_p2 = {
  "rock":{
    "rock": "Tied!",
    "paper": "%s wins!" % player_two,
    "scissors": "%s wins!" % player_one
  },
  "paper":{
    "rock": "%s wins!" % player_one,
    "paper": "Tied!",
    "scissors": "%s wins!" % player_two
  },
  "scissors":{
    "rock": "%s wins!" % player_two,
    "paper": "%s wins!" % player_one,
    "scissors": "Tied!"
  }
}

player_choose(player_index[0])
player_choose(player_index[1])
print player_index
winner = outcome_p1_p2[player_index[0]][player_index[1]]
print winner