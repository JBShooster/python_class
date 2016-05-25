#Joel Shooster
#HW 1 - Loops
#Date: 5/9/2016
#Loops.py

print "Name: Joel Shooster"
print "Section: HW 1 - Loops"
print "Date: 5/9/2016"
print "loops.py"

print "A loop that prints decimal equivalents..."
for x in xrange(1,11):
  print "1/%d converted to decimal is: " % x, 1.0 / x

print"\nNow a function that counts down from a user-selected, positive integer"
def get_num():
  valid = False
  while valid == False:
    try:
      num = input("Select a positive integer: ")
      if num > 1:
        countdown(num)
        valid = True
      elif num == 0:
        print "Zero? Really?"
      elif num == 1:
        print "Gotta be higher than 1."
      else:
        print "Negative number. Tsk tsk... "
    except (NameError, TypeError, ValueError, SyntaxError):
      print "That's not a valid integer"

def countdown(n):
  back_count = range(n,0,-1)
  for x in back_count:
    print x

def get_exp_and_base():
  invalid = True
  while invalid:
    try:
      print "\nLet's do an exponent."
      base = input("What is your base? : ")
      exp = input("What is your exponent? : ")
      if base > 0 and exp > 0:
        invalid = False
      elif base == 0 or exp == 0:
        print "Zero? Really?"
      else:
        print "Negative number. Tsk tsk... "
    except (NameError, ValueError, TypeError, SyntaxError):
        print "That's not a valid integer"
  for x in xrange(1,base + 1):
    print x, " ** %d =" % exp, x ** exp

def div_by_two():
  invalid = True
  while invalid == True:
    try:
      num = input("Give me something divisible by two: ")
      if num % 2 == 0:
        print "Yes! Divisible by two!"
        #Hey! The homework did ask for it to be witty. Right?
        invalid = False
      elif num == 0:
        print "Oh gosh... Not these zeroes again... "
      elif num % 2 != 0:
        print "Ummm.. NO!"
      else:
        print "Really? A negative number?"
    except (NameError, ValueError, TypeError, SyntaxError):
      print "That's not a valid integer"

get_num()
get_exp_and_base()
div_by_two()