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

c=0
for i in range(1, 10**6):
    l=[]
    if len(terminos_no_repetidos(i)) == 60:
        c=c+1
        
print c
     

