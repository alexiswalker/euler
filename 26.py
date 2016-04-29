import math
from fractions import Fraction

##print map(lambda x: format(1.0/x, '.1000f'), numbers)


def repeating(numerator, denominator, repeating_part=None):
    
    if repeating_part is None:
        repeating_part = []
        
    n = numerator*10
    
    if repeating_part.__contains__(n):
        if n == 0:
            return 0
        else:
            return len(repeating_part) - repeating_part.index(n)
    else:
        repeating_part.append(n)
        return repeating(n%denominator, denominator, repeating_part)

r = []
    
for i in range(2, 1000):
    r.append (repeating(1,i))
    
print max(r), r.index(max(r))+2
    
  