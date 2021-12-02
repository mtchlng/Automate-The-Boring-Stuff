
# THIS WHOLE THING IS BAD AND RUINED, JUST USE multiplyquiz.py INSTEAD


#prompt user with 10 questions
#range 1x1 to 9x9


#If correct, displays “Correct!” for 1 second and moves on to the next question.
#three tries for each question
#after　8　seconds the question is marked incorrect (even if they input the correct answer).

import pyinputplus as pyip
import random, time

x='''
In 30 seconds the math quiz will start.
There are 10 questions.
Each question will give you THREE TRIES
Each question has a time limit EIGHT SECONDS
'''
#time.sleep(30)

#USE (%s, %s) %(x, y)
#USE %s %x

correct = 0
for i in range(10):
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    answr = num1*num2
    print('%s x %s' %(num1, num2))
    try:
        result = pyip.inputStr(prompt='Enter Answer: ', limit=3, timeout=8, allowRegexes=['^%s$' %(answr)], blockRegexes=['.*', 'Incorrect'])
        correct+=1
    except: pyip.TimeoutException =print('exceeded available time')
    except: pyip.RetryLimitException =print('maximum number of tries reached')
    print(correct, 'correct out of', i+1, 'questions so far')

print(correct, 'correct out of', 10, 'questions')

#Use inputStr not inputNum so you have better control over what responses can be accepted
