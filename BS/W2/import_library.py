#library

#math library

import math  
print(math.log(10))
print(math.sin(90))
print(math.sqrt(9))
print(math.factorial(5))
print(math.pow(10, 3))

#random library

import random
print(random.random())  #random no. b/w 0 and 1

#Let us simmulate a coin toss.

import random
a = random.random()
if(a<0.5):
    print("Heads")
else:
    print("Tails")


#Let us simulate a dice

import random
dice1 = (random.randrange(1, 7))
dice2 = (random.randrange(1,7))
total = dice1 + dice2

print("Your pair of dice is: ", total)

# calendar library

import calendar
print(calendar.month(2026, 2))
print(calendar.calendar(2026))

from calendar import *
print(month(2026, 10))
print( calendar(2026))