# Multiplication math quiz
#allowregexes, blockregexes, timeout, limit keywords
#10 random problems
#keep track of number of questions
#keep track of number of correct answers

import pyinputplus as pyip
import random, time

numberQuestions = 0
numberCorrect = 0

for numberQuestions in range(10):
    numberQuestions += 1
    num1 = random.randint(0,11)
    num2 = random.randint(0,11)
    prompt = '#%s: %s x %s = ' % (numberQuestions, num1, num2)
    try:
        pyip.inputStr(prompt,
        allowRegexes=['^%s$' %(num1*num2)],
        blockRegexes=[('.*', 'Incorrect')],
        timeout=8, limit=3)
    except pyip.TimeoutException: print('Out of time')
    except pyip.RetryLimitException: print('Out of tries')

    else:
        print('Correct')
        numberCorrect += 1
    time.sleep(1) #Brief pause to let user read the result
print('Score: %s / %s' % (numberCorrect, numberQuestions))
