from math import factorial
  
def suma_factorial_digitos(numero):
    return sum(map(factorial,map(int,str(numero))))

l=[]
def terminos_no_repetidos(numero):
    if l.__contains__(numero):
        return l
    else:
        l.append(numero) 
        suma = suma_factorial_digitos(numero)
        return terminos_no_repetidos(suma)
        
print terminos_no_repetidos(540)
  