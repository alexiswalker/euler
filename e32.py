from itertools import permutations, combinations

def es_pandigital(n):
    return ''.join(sorted(n)) == '123456789'

permutation = [''.join(i) for i in permutations('123456789', 1)]
permutation = permutation + [''.join(i) for i in permutations('123456789', 2)]
permutation = permutation + [''.join(i) for i in permutations('123456789', 3)]
permutation = permutation + [''.join(i) for i in permutations('123456789', 4)]

combination = combinations(permutation, 2)

resultado = [(i[0], i[1],str(int(i[0])*int(i[1]))) for i in combination if es_pandigital(''.join((i[0], i[1],str(int(i[0])*int(i[1])))))]

print sum(set([int(i[2]) for i in resultado]))