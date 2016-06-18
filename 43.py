from itertools import permutations

digits = '0123456789'

def  is_divisible_by(number, divisor):
    return number % divisor == 0

def property(string):
    return reduce(lambda x, y : x and y,  [is_divisible_by(int(string[index+1:index+4]), i) for index, i in enumerate([2,3,5,7,11,13,17])])
    
print property('1406357289')

print sum([int(''.join(i)) for i in permutations(digits) if property(''.join(i))])