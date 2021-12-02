#How to keep an idiot busy for hours

# 1. Ask the user if theyd like to know how to keep an idiot busy for hours
# 2. If user answers no, quit
# 3. If user answers yes, go to step one

import pyinputplus as pyip

while True:
    #prompt='Do you want to know how to keep an idiot busy for hours?\n'
    #response = pyip.inputYesNo(prompt)
    response = pyip.inputYesNo('Do you want to know how to keep an idiot busy for hours?\n')
    if response == 'no':
        print('Thank you, have a nice day')
        break

JapaneseVersion = '''
while True:
    response = pyip.inputYesNo('バカの困らせる方法を知りたいか？',yesVal='はい', noVal='いいえ')
    if response == 'いいえ':
        print('了解、良い1日を〜')
        break
'''
