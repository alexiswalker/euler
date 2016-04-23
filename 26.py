import math
from fractions import Fraction

##print map(lambda x: format(1.0/x, '.1000f'), numbers)

l = []

def repeating(numerator, denominator):
    n = numerator*10
    
    if l.__contains__(n):
        if n == 0:
            return 0
        else:
            return len(l) - l.index(n)
    else:
        l.append(n)
        repeating(n%denominator, denominator)

r = []
    
for i in range(2, 1001):
    l = []
    print repeating(1,i)
    