# Name:
# Section:
# strings_and_lists.py
# **********  Exercise 4.1 **********
def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num
    return total
# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])

#Cumulative sum: Create a new list where each item is the sum
# of the previous numbers plus current
def cumulative_sum(number_list):
    sum = []
    total = 0
    for x in number_list:
        total += x
        sum.append(total)
    print sum

#Test Cases
print "\ncumulative_sum([1,2,3])"
cumulative_sum([1,2,3])
print "\ncumulative_sum([4,3,6])"
cumulative_sum([4,3,6])
print "\ncumulative_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])"
cumulative_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# **********  Exercise 4.2 **********
# Write any helper functions you need here.
# Below function accounts for both HW2 pig-latin and the optional pig-latin add-ons

VOWELS = ['a', 'e', 'i', 'o', 'u']
import string

def pig_latin():
    n = raw_input("\nEnter a phrase. Go ahead. Use numbers & punctuation if you want.\nWatch what happens:\n").lower()
    exclude = set(string.punctuation) # Targeting punctuation
    n = "".join([i for i in n if not i.isdigit()]) #Stripping numbers away
    n = "".join(i for i in n if i not in exclude) #Stripping punctuation away
    words = n.split(" ")
    result = []
    for x in words:
        if x[0].lower() in VOWELS:
            word = (x + "hay")
            result.append(word)
        else:
            end_char = x[0].lower()
            word = (x[1:] + end_char + "ay")
            result.append(word)
    for j in result:
        print j
pig_latin()

# **********  EXTRA! Optional Part 2 *********
#This helps us find how many elements in a list are integers
print "\n2.1\nList Comprehension Challenges\nFind integers in list\nThis helps us find how many elements in a list are integers:\n"
def find_ints(n):
    print [x for x in n if isinstance(x, int)]

print "find_ints(['Hello']): "
find_ints(["Hello"])
print "\nfind_ints([12345]): "
find_ints([12345])
print "\nfind_ints(['Hello', 12345, 4938, 23423, 0, 'LOL']): "
find_ints(["Hello", 12345, 4938, 23423, 0, "LOL"])

#2.2
print"\n2.2 Range\n"
x = [num for num in range(-5,6)]
y = [num for num in range(0,11)]
print [[i, i**2+1] for i in x if i**2+1 in y ]

#2.3
print "\n2.3 Radius\n"
radius = 5
print [[i, radius**2 - i**2] for i in x if radius**2 - i**2 in y ]



