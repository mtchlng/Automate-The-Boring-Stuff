#8+ characters long
#Both upper and lower case
#At least one digit

#Weak: meets none of the conditions
#Moderate: meets one of the conditions
#Strong: Meets all 3 of the conditions

# 1 | 2 | 3: Weak
# 1 & 2 | 1 & 3 | 2 & 3 : Moderate
# 1 & 2 & 3 : Strong

#condOne = [a-zA-Z0-9_.-@]{8} #8+ characters long
#condTwo = [a-z].*[A-Z]|[A-Z].*[a-z]#Upper lower
#condThree = \d #At least one digit
#Condition two should really be 2 conditions, upper and lower case are two separate conditions

#condOne|condTwo|condThree
#Q if there are two conditions being met wouldnt this "one condition" ergex still apply...?
#condOne&condTwo|condOne&condThree|condTwo&condThree
#Ampersand is not recognized by regex... what should I do?
#condOne&condTwo&condThree
#Ampersand is not recognized by regex... what should I do?
import re
def strong_password(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print('Password too weak')
            break
        else:
            regex_count += 1
            continue
    if regex_count == 4:
        print('Password is strong')

regex1 = re.compile('.{8}') #why comma?
regex2 = re.compile('[a-z]') #why plus?
regex3 = re.compile('[A-Z]') #why plus?
regex4 = re.compile('[\d]')
regex_list = [regex1, regex2, regex3, regex4]

#pwList = ['testpw', 'Testpw', 'TESTPW', 'TESTPW123', 'Testpw123', 'TESTPW123!@#','Tb1@Tb1@', 'TestPW123', '!@345ssfe@#23T4']
#for x in pwList: strong_password(x)

x=input('Please input a password to test: ')
strong_password(x)
