#write a function doing same thing as strip () string method
#if only 1 argument: whitspace characters will be removed from the beginning/end of string
#if 2 arguments: characters spectified in the second argument will be removed from string

mystring=input('Enter a string of text to strip: ')
mychar=input('Enter a character to remove (press Enter for whistespace)')


def regexStrip(str, char):
    import re
    if char != '':
        char=re.compile(char)
        newstr = char.sub('',str)
    else:
        char = re.compile(r'^\s*')#left
        newstr = char.sub('', str)
        char = re.compile(r'\s*$')#right
        newstr = char.sub('', newstr)

        #char=re.compile(r'(^\s)*([a-zA-Z0-9\s])*(\s$)*') #find lines with whitespace on either side of text
        #Q: even if i can find the character using regex how does that help? I cant edit the string.
        #Q I can only create a new copy of the string without the whitespace
        #A: USE THE 'SUB' METHOD!!
        #newstr = char.findall(str)[1]  #remove the whitespace OR char from these lines
    return newstr


print(regexStrip(mystring, mychar))
