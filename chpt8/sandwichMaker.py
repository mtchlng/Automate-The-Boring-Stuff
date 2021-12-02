import pyinputplus as pyip

breadR = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Input bread type: \n', numbered=True)
meatR = pyip.inputMenu(['chicken','turkey','ham','tofu'], prompt='Input meat: \n')
cheeseR = pyip.inputYesNo(prompt='Want cheese?\n')
if cheeseR == 'yes':
    cheeseR = pyip.inputMenu(['cheddar','swiss','mozzarella'], prompt='Input cheese: \n')
mayoR = pyip.inputYesNo(prompt='Want mayo? \n')
mustardR = pyip.inputYesNo(prompt='Want mustard? \n')
lettuceR = pyip.inputYesNo(prompt='Want lettuce? \n')
tomatoR = pyip.inputYesNo(prompt='Want tomato? \n')
quantityR = pyip.inputInt(prompt='How many sandiwches u want? \n', min=1)

price = 500

if meatR == 'turkey':
    price+=53
    print('Added turkey for 53')
if cheeseR != 'no':
    price+=61
    print('Added cheese for 61')
if mayoR == 'yes':
    price+=25
    print('Added mayo for 25')
if mustardR == 'yes':
    price+=30
    print('Added mustard for 30')
if tomatoR == 'yes':
    price+=84
    print('Added tomato for 84')


if quantityR == 1:
    print('The price of your sandwich is', price, '. Have a nice day! :)')

if quantityR > 1:
    price *= quantityR
    print('Your price for ', quantityR, 'sandwiches is ', price, '. Have a nice day! :)')
