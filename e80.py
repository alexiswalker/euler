from math import * 
from decimal import *

getcontext().prec = 109

def cien_primeros_digitos(numero):
    raiz = Decimal(numero).sqrt()
    return str(raiz*10**99)[:100] if raiz % 1 !=0 else '0'

def suma_cien_primeros_digitos(digitos):
    return sum(map(int, digitos))

def resultado():
    return sum([suma_cien_primeros_digitos((cien_primeros_digitos(i))) for i in range(1, 101)])

if __name__ == '__main__':
    print cien_primeros_digitos(2)

