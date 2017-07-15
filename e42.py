from math import sqrt

def es_triangulo(numero):
    return ((-1+sqrt(8*numero+1))/2).is_integer()

def letras():
    return [chr(i) for i in range(ord('A'),ord('Z')+1)]

def indice_letra(letra):
    return letras().index(letra)+1

f = open('p042_words.txt', 'r')
archivo = f.read().replace('"', '').split(',')
f.close()


resultado = 0

for palabra in archivo:
    c=0
    for caracter in palabra:
        c+=indice_letra(caracter)

    if es_triangulo(c):
        resultado +=1

print resultado
#return sorted(names.split(','))