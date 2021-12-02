# Get the text off the clipboard
# Find all phone numbers and email addresses in the text
# Paste them onto the clipboard

# Steps:
# Use the pyperclip module to copy / paste strings
# Create two regexes, one for phone # and one for emails
# Find ALL matches, not just the first matches
# Neatly format the matches strings into a single string to paste
# Display some message if no matches found

#! python3
# extractor.py - Finds phone numbers and emails in the clipboard
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   #optional area code: 3 numbers OR (3 numbers in parenthesis), ? makes it match 0 or 1 of these instances
    (\s|-|\.)?          #optional separator: space char OR hyphen OR period
    (\d{3})             #middle 3 digits
    (\s|-|\.)           #separator: space char OR hyphen OR period
    (\d{4})             #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #optional extension: optional space, ext/x/ext, optional space, two to five digits
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username: can include letters upper & lower, numbers, dots, dashes, underscores, percent sign, plus signs
    @
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #dot something, 2 to 4 letters
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #joins separators and the extension
    if groups[8]!= '' :
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
