# Read text files
# lets user add text where ADJECTIVE / NOUN / ADVERB / VERB appears

#read madlib.txt
#save it as new file
#overwrite this file

#A new file can be created by passing a file name that does not exist.
#madlibnew.txt

import re
#open madlibs file
file = open(r"/Users/langework/Desktop/ATBS/chpt9/madlib.txt")
#save contents so you can modify it
text = file.read()
file.close()

regex = re.compile(r'(NOUN)|(VERB)|(ADVERB)|(ADJECTIVE)') #searches for 4 regex groups

for matches in regex.findall(text): #"matches" is all matched groups
    for j in matches: #checks each matched group for multiple matches
        if j !='':
            reg = re.compile(r'{}'.format(j))
            inp_text = input('Enter the substitute for %s: ' %j)
            text = reg.sub(inp_text, text, 1)

print(text)

file = open('madlibNEW.txt', 'w')
file.write(text)
file.close()
