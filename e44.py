from math import sqrt
from itertools import combinations

def es_pentagono(number):
    return ((1 + sqrt(24*number + 1))/6).is_integer()

def pentagono(numero):
    return numero*(3*numero-1)/2


i=1
b=True
while b:
    i+=1
    pentagono_i = pentagono(i)
    for j in range(i)[:0:-1]:
        pentagono_j = pentagono(j)
        if es_pentagono(pentagono_i+pentagono_j) and es_pentagono(pentagono_i-pentagono_j):
            print i, j, pentagono_i, pentagono_j, pentagono_i-pentagono_j
            b=False
            break

#c =100000000

#pentagonos = [i for i in range(c+1)[1:] if es_pentagono(i) ]


#print [i for i in combinations(pentagonos,2) if es_pentagono(i[0]+i[1]) and es_pentagono(abs(i[0]-i[1]))]