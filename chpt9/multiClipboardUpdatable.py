#command line argument for the keyword is checked
#if the argument is "save": clipboard contents are saved to the keyword
#If the argument is "list": all keywords are copied to the clipboard
#OTherwise, the text for the keyword is copied to the clipboard

#! python３
# multiClipboaradUpdatable.py - Saves and loads pieces of text to the clipboard
# How to Use:
#   py.exe multiClipboaradUpdatable.py save <keyword> - Saves clipboard to keyword
#   py.exe multiClipboaradUpdatable.py <keyword> -  Loads keyword to clipboard
#   py.exe multiClipboaradUpdatable.py - Loads all keywords to clipboard

import shelve, pyperclip, sys #pyperclip is for copy/pasting, sys is dor reading the command line arguments
mcbShelf = shelve.open('mcb')

#TODO Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    #If the 1st command line argument (which will always be at index 1 of sys.argv list) is 'save', the 2nd command line argument is the keyword for the current content of the clipboard.
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
    elif sys.argv[1].lower() = 'deleteall':
        for x in list(mcbShelf.keys()):
            del mcbShelf[x]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
