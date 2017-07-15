from euler_util import *

def cantidad_elementos_anterior_a_superar_limite(primos, limite, indice_primera_posicion):

    cantidad_elementos = len(primos[indice_primera_posicion:])
    for i in range(cantidad_elementos):
        if sum(primos[indice_primera_posicion:indice_primera_posicion+i+1]) > limite:
            return i

    return cantidad_elementos

def cantidad_elementos_suma_es_primo(primos, indice_primera_posicion, cantidad_elementos):
    for i in range(len(primos))[cantidad_elementos:0:-1]:
        if is_prime(sum(primos[indice_primera_posicion:indice_primera_posicion+i])):
            return i

limite = 1000000
primos = [i for i in primes_sieve(limite)]

m = 0
for i in range(len(primos)):
    l = cantidad_elementos_anterior_a_superar_limite(primos, limite, i)
    if l < m:
        continue
    c = cantidad_elementos_suma_es_primo(primos, i, l)
    if c > m:
        m = c
        p = i

print (m,p,sum(primos[p:p+m]))

