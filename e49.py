from euler_util import is_prime

def completar_ceros(numero):
    temp = '0000'+str(numero)
    return temp[len(temp)-4:]

def ordernar_caracteres(string):
    return ''.join(sorted(string))

p = [i for i in range(3340)][1:]
s = map(lambda x : x+3330,p)
t = map(lambda x : x+3330,s)

sp = map(lambda x : ordernar_caracteres(completar_ceros(x)), p)
ss = map(lambda x : ordernar_caracteres(completar_ceros(x)), s)
st = map(lambda x : ordernar_caracteres(completar_ceros(x)), t)

for i in range(3339):
    if sp[i]==ss[i] and ss[i]==st[i] and is_prime(i+1)and is_prime(i+1+3330) and is_prime(i+1+3330*2):
        print i+1, i+1+3330, i+1+3330*2, sp[i], ss[i], st[i]