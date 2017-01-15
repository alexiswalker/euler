from itertools import combinations, groupby
from math import sqrt
import collections

numeros = range(1001)[1:]

combinaciones_2 = [i for i in combinations(numeros, 2)]

lados_triangulo_rec = [(i[0], i[1], sqrt(i[0]**2+i[1]**2)) for i in combinaciones_2] 

lados_enteros_que_suma_menos_de_mil = [i for i in lados_triangulo_rec if i[2].is_integer() and sum(i) < 1000]

suma_de_lados = [sum(i) for i in lados_enteros_que_suma_menos_de_mil]

frecuencia=collections.Counter(suma_de_lados)

mayor_frecuencia = frecuencia.most_common(1)


print mayor_frecuencia







