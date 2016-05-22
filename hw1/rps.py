#Joel Shooster
#HW 1 - Rock Paper Scissors
#Date: 5/9/2016
#rps.py

print "Name: Joel Shooster"
print "Section: HW 1 - Rock Paper Scissors"
print "Date: 5/9/2016"
print "rps.py"

#This is rock/paper/scissors
print"Welcome to Rock / Paper / Scissors! Such a fun game!\n"

player_one = raw_input("Player 1 name?: ")
print "Welcome, ", player_one
print""

player_two = raw_input("Player 2 name?: ")
print "Welcome, ", player_two
print""

possible_choices = ['rock', 'paper', 'scissors']
player_choices = ["", ""]

def player_one_choose():
  choice = raw_input(player_one + ". Rock, paper or scissors?: ")
  if choice not in possible_choices:
    print "That isn't a valid option"
    player_one_choose()
  else:
    player_choices[0] = choice

def player_two_choose():
  choice = raw_input(player_two + ". Rock, paper or scissors?: ")
  if choice not in possible_choices:
    print "That isn't a valid option"
    player_two_choose()
  else:
    player_choices[1] = choice

print player_choices

def who_won(n):
  one = n[0]
  two = n[1]
  if one == "rock" and\
    two == "rock":
    print "Tied!"
  elif one == "paper" and\
    two == "paper":
    print "Tied!"
  elif one == "scissors" and\
    two == "scissors":
    print "Tied!"
  elif one == "rock" and\
    two == "scissors":
    print player_one, " wins!"
  elif one == "scissors" and\
    two == "paper":
    print player_one, " wins!"
  elif one == "paper" and\
    two == "rock":
    print player_one, " wins!"
  elif two == "rock" and\
    one == "scissors":
    print player_two, " wins!"
  elif two == "scissors" and\
    one == "paper":
    print player_two, " wins!"
  elif two == "paper" and\
    one == "rock":
    print player_two, " wins!"

player_one_choose()
player_two_choose()
print player_choices
who_won(player_choices)
print""