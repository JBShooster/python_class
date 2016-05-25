#Joel Shooster
#5.10.16
#Zellers.py

MONTHS = [11,12,1,2,3,4,5,6,7,8,9,10]
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def date_finder(month, day, year, century):
  part_one = (13*month-1) / 5
  part_two = year / 4
  part_three = century / 4
  part_four = part_one + part_two + part_three + day + year - (2*century)
  return part_four % 7

def get_info():
  valid = False
  while valid == False:
    try:
      first_name = raw_input("Enter your first name: ")
      last_name = raw_input("Enter your last name: ")
      month = input("What month were you born? (please choose between 1 and 12, no zeroes): ")
      day = input("Day? ")
      year = input("Year? (XXXX format) ")
      print month
      if month >=1 and month <= 12:
        valid = True
      else:
        print "That's not a valid selection"
    except (NameError, ValueError, TypeError, SyntaxError):
      print "That's not a valid integer"

  print "You are %s %s. You were born %s / %d / %d"  % (first_name, last_name, month, day, year)
  print "Month: ", month
  month = MONTHS[month-1]
  year = str(year)
  century = int(year[:2])
  year = int(year[-2:])
  print "Century: ", century
  print "Year: ", year
  if month == 11 or month == 12:
    year = year - 1

  result = date_finder(month, day, year, century)
  print "\n%s %s was born on a %s" % (first_name, last_name, DAYS[result])

print "We will return the day of the week in which you were born"
print "Sunday is 0, Monday is 1, Tuesday is 2, etc..."
get_info()