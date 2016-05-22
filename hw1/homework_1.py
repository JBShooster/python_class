print "Name: Joel Shooster"
print "Section: HW 1"
print "Date: 5/9/2016"
print "homework_1.py"
print ""
##### Template for Homework 1, exercises 1.2-1.4 ######

print "********** Exercise 1.2 **********"

print "Made the board into a variable so we can reuse it"

board = """
          |  |
        --------
          |  |
        --------
          |  |
"""
print board

print "********** Exercise 1.3 **********"
print"""If we want to make the board more than just a string, we ought to use
format strings to put some life into it. I turned the boxes into indeces on a tuple.
Below we have an empty board. However, this time it has 9 boxes ready to by used in a game.
"""

boxes = ["-","-","-","-","-","-","-","-","-"]
board = """
         %s | %s | %s
        ------------
         %s | %s | %s
        ------------
         %s | %s | %s
"""

print board % tuple (boxes)


print "For fun, let's change those box variables and see what happens when we run board again."
boxes = ["x", "o" , "o", "-", "x", "o", "-", "-", "x"]
boxes[3] = "o"
boxes[6] = "o"
boxes[7] = "x"

print board % tuple(boxes)
print "Not so empty anymore, huh?"
print "Now let's demonstrate how we could get user input...."

print "********** Exercise 1.4 **********"

def get_info():
  first_name = raw_input("Enter your first name: ")
  last_name = raw_input("Enter your last name: ")
  dob = raw_input("Enter your date of birth: ")
  month = raw_input("Month? ")
  day = input("Day? ")
  year = input("Year? ")
  print"""
  You are %s %s. You date of birth is %s.
  The month is %s. Day is %d. Year is %d.
  """ % (first_name, last_name, dob, month, day, year)

get_info()
