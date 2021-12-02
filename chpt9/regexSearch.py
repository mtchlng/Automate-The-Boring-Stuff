#!python3
#open all .txt files in a folder
#searches for any line that matches an inputted regex
#print matches to screen

#NOTE: for some reason, matches aren't properly being displayed to screen.


import glob, os, re
text=''

dir = input('Input directory: ')
if len(dir) < 1: dir = '/Users/langework/Desktop/ATBS/chpt9'
os.chdir(dir)

input = input('Input regular expression: ')
regex = re.compile(input)

#Find all txt files in the specified directory and paste contents into variable 'text'
for txtfile in glob.glob('*.txt'):
    file = open(txtfile, 'r')
    fhand = file.read()
    file.close()
#    text += str(fhand)

#for each txt file found,
    result = regex.search(fhand)
    if result == None:
        print('No matching content found')
        break
    elif result.group() != None:
        print('Content found in file: ', (os.path.abspath(txtfile)))
        print('Content found: ', result)
    file.close()

x = '''

#Take the contents from txt files (variable 'text') and input it into new file
file = open('regexResults.txt', 'w')
file.write(text)
file.close()
'''
