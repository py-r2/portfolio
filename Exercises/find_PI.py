'''This short program is intended to find PI with as many decimals
as your input number (this number will have a limitation)'''
from __future__ import division
import math
while True:

    decimals = int(raw_input('Please enter a decimals number between 1 - 30:'))
#    x = 9876 # the bigger x the most accurate pi will be
#    pi = x * math.sin(math.radians(180 / x))
    pi = '3.141592653589793238462643383279'
    if decimals >= 1 and decimals <= 30:
        print pi[0:(decimals+2)]
        break
    else:
        print "Your input number is not between 1 and 30 as requested! \
        Please try again."
