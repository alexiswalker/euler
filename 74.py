from math import factorial
  
def suma_factorial_digitos(numero):
    return sum(map(factorial,map(int,str(numero))))

def terminos_no_repetidos(numero, terminos=None):
    if terminos is None:
        terminos = []
        
    if terminos.__contains__(numero):
        return terminos
    else:
        terminos.append(numero) 
        suma = suma_factorial_digitos(numero)
        return terminos_no_repetidos(suma, terminos)

print terminos_no_repetidos(69)

c=0
for i in range(1, 10**3):
    if len(terminos_no_repetidos(i)) == 60:
        c=c+1
        
print c
     

