from euler_util import is_prime

def divisores(numero):
    r=[1,numero]
    return r + [i for i in range(2,numero / 2 + 1) if not numero%i]

def divisores_primos(numero):
    return [i for i in divisores(numero) if is_prime(i)]

start = 2*3*5*7
n = 4
c = 1
while c < n:
    start+=1
    if len(divisores_primos(start))==n:
        c+=1
    else:
        c=0

print start

        


