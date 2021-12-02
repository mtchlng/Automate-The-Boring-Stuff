#get text from clipboard
#add a star and space to beginning of each line
#paste this new text to the clipboard

#! python3
# bulletPoint Adder.py - ADds wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste() #returns all text in clipboard as one big string
# separate lines and add stars
lines = text.split('\n')
for i in range (len(lines)): #loop through lines lsit
    lines[i]='*'+lines[i] #add a star to each string
text = '\n'.join(lines)
pyperclip.copy(text)
