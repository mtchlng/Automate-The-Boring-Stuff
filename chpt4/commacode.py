#take lsit as argument
#return string with all items separated by comma, space, "and" before last item

# DAMN this shit took me an hr and 7 min

def stringify(mylist):
    mylist.insert(-1, "and ")
    mystring = ''
    i = 0
    while i < len(mylist):
        if i == (len(mylist)- 2) :
            mystring += (mylist[i] + mylist[-1])
            break
        else:
            mystring += (mylist[i] + ', ')
            i += 1
    print(mystring)

lst = input('Gimme a list!')
if len(lst) < 1: lst = ['apples', 'bananas', 'tofu', 'cats']
stringify(lst)
