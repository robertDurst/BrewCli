import sys, tty
from Alphabet import convert_character_to_hebrew

import getch
buffer = ''
while True:
    x = getch.getch()
    if x == "\n":
        buffer = ''
        print("")
        continue
    nextchar = convert_character_to_hebrew(x)
    if nextchar != '':
        print(nextchar+buffer, end='\r', flush=True)
        buffer = nextchar + buffer