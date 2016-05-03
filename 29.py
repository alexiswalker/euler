from itertools import *

n = 2
m = 100

r = range(n, m+1)

s =set()

for i in product(r, repeat=2):
    s.add(pow(i[0],i[1]))
    #s.add(sum(map(pow,i, r)))
    
print len(s)