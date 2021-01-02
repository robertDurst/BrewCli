import getch, json, sys, tty
from alphabet import convert_character_to_hebrew

# open dictionary file and load
with open('data/dictionary.json') as f:
  data = json.load(f)
hebrew_dictionary = {}
for word in data:
    meaning = data[word]
    # this is due to odd reason terminal one direction and saved file reverse
    word = word[::-1]
    hebrew_dictionary[word] = meaning

# read a word, translating each character as the user types then check to see if it exists in the dictionary
buffer = ''
running = True
while running:
    x = getch.getch()
    if x == "\n":
        if buffer in hebrew_dictionary:
            print(buffer + ": " + hebrew_dictionary[buffer])
        else:
            print(buffer + " not in dictionary, considering adding (copy and paste the following): " + buffer[::-1])
        running = False
    nextchar = convert_character_to_hebrew(x)
    if nextchar != '':
        print(nextchar + buffer, end='\r', flush=True)
        buffer = nextchar + buffer