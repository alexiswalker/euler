def es_pandigital(number):
    return ''.join(sorted(str(number))) == '123456789'


for i in range(9123,9876+1)[::-1]:
    if es_pandigital(i*100000+i*2):
        break

print i, i*100000+i*2