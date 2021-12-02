#Write down how often a streak of 6 heads or 6 tails comes up in a random lists
#1st part: generate a list of randomly selected ' \heads' and 'tails' values
#2nd part: check for streaks
#repeat 10,000 times

import random
numberOfStreaks = 0
headstreakcount = 0
tailstreakcount = 0
mylist = []
for experimentNumber in range(10000):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    mylist.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    #does this by using a separate count for streaks
    if mylist[experimentNumber] == 0:
            headstreakcount +=1
            tailstreakcount = 0
    else:
            headstreakcount = 0
            tailstreakcount += 1
    if headstreakcount == 6 or tailstreakcount == 6:
        numberOfStreaks +=1
        print("Streak Found!" + str(experimentNumber))

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
