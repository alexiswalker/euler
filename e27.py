from euler_util import is_prime

def primos_entre(i,f):
    return [i for i in range(i,f+1) if is_prime(i)]

#b = primos_entre(2, 1000) 
#c = map(lambda x : x*-1,b)
if __name__ == '__main__':
    max  = 0
    for a in range(-999,999+1):
        for b in primos_entre(-1000,1000):
            n = 1
            while is_prime(n**2+a*n+b):
                n= n +1
            if n > max:
                maxa =a
                maxb=b
                max = n

print maxa, maxb, maxa * maxb 