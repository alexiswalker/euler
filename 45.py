#triangle = list()	
pentagonal = list()
hexagonal = list()

n = 0
c = 0

while c < 3 :

    n = n + 1
    
    t = n*(n+1)/2
    p = n*(3*n-1)/2
    h = n*(2*n-1)
    
    #triangle.append(t)
    pentagonal.append(p)
    hexagonal.append(h)

    if pentagonal.__contains__(t) and hexagonal.__contains__(t):
        print t
        c = c + 1
    


