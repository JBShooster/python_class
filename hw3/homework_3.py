# Name: Joel Shooster
# Section: HW3
# homework_3.py


##### Template for Homework 3, exercises 5.1 - 5.5 ######

# **********  Exercise 5.1 **********

# Bugs
##### BUG 1 #####
print "Bug 1: large_num doesn't return anything. Should return True or False\n"

##### BUG 2 #####
print "Bug 2: The function does not handle non-int inputs properly.\n"

##### BUG 3 #####
print "Bug 3: Variables b and num are not defined."


# **********  Exercise 5.2 **********

# Define "Mutable" and list what data structures have this characteristic
print"""
Mutable objects are objects in which one can change the values.
They can be changed in place.
Mutable objects include sets, dictionaries, lists, and byte arrays.
"""

#Examples
name = ["Joel"]
name.append("Shooster")
print name

# Define "Immutable" and list what data structures have this characteristic
print"""
Immutable objects cannot be changed. Cannot be changed in place.
Examples include strings, tuples, bytes, booleans, frozen sets, integers, floats, long.
"""

#Examples
me = ("Joel")
print "me = ('Joel')"
print "me is a tuple. I can't say me[1] = ' Shooster'"
print "However, I can say me = me + ' Shooster'"
me += " Shooster"
print "That would return:", me #Expect Joel



# **********  Exercise 5.3 **********
import math
print "\nBall Collision:\n"
def ball_collide(ball1, ball2):
    distance = math.sqrt((ball1[0]-ball2[0])**2 + (ball1[1]-ball2[1])**2 )
    return (distance <= ball1[2] + ball2[2])

# Test Cases for Exercise 5.3
print "ball_collide((0,0,1), (3,3,1)) => Expect False"
print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False

print "\nball_collide((5,5,2), (2,8,3))) => Expect True"
print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True

print "\nball_collide((7,8,2), (4,4,3))) => Expect True"
print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True

# **********  Exercise 5.4 **********
my_classes = {
    101: "Space Age Engineering with Professor Musk",
    303: "Europa Biology with Dr. Neil deGrasse Tyson"
    }

def add_class(class_num, desc, class_dict):
    '''
    Adds a class number/class name pair to a dictionary

    class_num: a string; the MIT number associated with the class
    desc: a string; the English name of the class
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; only modifies class_dict
    '''
    class_dict[class_num] = desc

#Let's add a few classes
add_class(204, "Vocal training with Beyonce", my_classes)
add_class(202, "Governing a country with Professor Obama", my_classes)
add_class(405, "Advanced Mutant Combat with Dr. Jean Grey", my_classes)


def print_classes(course, class_dict):
    '''
    Prints out all the classes you've taken in a given Course.
     If no classes were taken in the Course, print out that none were taken

    course: a string; the Course for which we would like to
     print out classes taken
    class_dict: a dictionary with the keys being class numbers
     and the values being class names

    returns: nothing; simply prints out relevant information
    '''
    count = 0
    for x in class_dict:
        if course in class_dict[x]:
            print class_dict[x]
            count = count + 1
    if count == 0:
        print "Courses with %r not found" % course

print "\nChecking your schedule for the following classes: 'Tyson', 'Grey', and 'Trump'\n"
print_classes("Tyson", my_classes)
print_classes("Grey", my_classes)
print_classes("Trump", my_classes)

# **********  Exercise 5.5 **********

def build_addr_book(fileName):
    address_book = {}
    try:
        addresses = open(fileName, "r")
        for line in addresses:
            line = line.strip("\n")
            line = line.split(',')
            name = line[0] + "," + line[1]
            address_book[name] = line[2:]
        addresses.close()
        return address_book
    except (IOError, ValueError):
        print "This file was not found."

my_book = build_addr_book("rawAddresses.csv")

def change_entry(addr_book, entry, field, newValue):
    addr_book_keys = addr_book.keys()
    if field == "newEntry":
        addr_book[entry] = newValue
    elif entry not in addr_book_keys:
        print "This entry does not exist. Try again."
    elif field == "name":
        value = addr_book[entry]
        del addr_book[entry]
        addr_book[newValue] = value
    elif field == "phoneNumber":
        addr_book[entry][0] = newValue
    elif field == "emailAddress":
        addr_book[entry].append(newValue)
    else:
        print "That field does not exist."
    # print "\nChanges made:\n", newValue, ": ", addr_book[newValue]

#Let's find Barack Obama
print "\nBarack Obama's information:"
print "printing my_book['Obama,Barack']\n"
print my_book["Obama,Barack"]

change_entry(my_book, "Obama,Barack", "name", "Clinton,Hillary")
print my_book.keys()

print "\nBarack Obama has been replaced by Hillary Clinton. Now let's add her email!"
change_entry(my_book, "Clinton,Hillary", "emailAddress", "hillary@us.gov")
print "UPDATE - Hillary Clinton: ", my_book["Clinton,Hillary"]

print "\nNow her phone number:"
change_entry(my_book, "Clinton,Hillary", "phoneNumber", "1-222-555-9999")
print "UPDATE - Hillary Clinton: ", my_book["Clinton,Hillary"]

print "\nNow let's break this by putting change_entry with 'Clinton, Bill' as our entry"
change_entry(my_book, "Clinton,Bill", "phoneNumber", "1-222-555-9999")

print "\nNow let's add a new value. Elon Musk"
change_entry(my_book, "Musk,Elon", "newEntry", "['555-123-4567', 'elon@tesla.com']")
print "my_book['Musk,Elon'] =>", my_book["Musk,Elon"]

print "\nSee Elon and Hillary in the index: ", my_book.keys()

