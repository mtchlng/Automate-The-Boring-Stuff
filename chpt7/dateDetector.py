#Date Detector
#python3

#detect dates in DD/MM/YYYY format
#single digit days/months start with 0

import re

dateDetector = re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/([12]\d\d\d)')
#(0[1-9]|1[0-2]/)(0[1-9]|1[0-2]/)([1-2][1-9]{1,3})

x = input("Enter text to search for dates")
if len(x)<1: x='Enter text to search for datesto detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021'

y = dateDetector.findall(x)
y.group(0)
#str = '/'.join(y)

#why is this not returning matched dates?!
