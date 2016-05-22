#Joel Shooster
#5.10.2016
#Message Cipher

LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
PUNCTUATION = "!@#$%^&*()-[]}{|\/.,><~`;:'\"?"
#This is where we set the shift value. Right now it's set to 4.
SHIFT = 4

# Now let's parse through the user's input. It can handle lowercase letters,
# uppercase letters, punctuation, and integers.
cipher = ""
text = raw_input("Enter message. Don't be shy. \nUse whatever characters you want. We can translate it: ")
for x in text:
  if x in LETTERS:
    letter_index = (LETTERS.index(x)+SHIFT)%(len(LETTERS))
    cipher += LETTERS[letter_index]
  elif x in UPPER_LETTERS:
    upper_index = (UPPER_LETTERS.index(x)+SHIFT)%(len(UPPER_LETTERS))
    cipher += UPPER_LETTERS[upper_index]
  elif x in NUMBERS:
    x = NUMBERS[(NUMBERS.index(x)+SHIFT)%(len(NUMBERS))]
    x = int(x) % 6
    x = str(x)
    cipher += x
  elif x == " ":
    cipher += " "
  elif x in PUNCTUATION:
    cipher += x
print("Your message: " + cipher)