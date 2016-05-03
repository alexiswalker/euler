from itertools import *

n = 2
m = 100

r = range(n, m+1)

s = set([pow(i[0],i[1]) for i in product(r, repeat=2)])

print len(s)

##9183