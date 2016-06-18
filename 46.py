from euler_util import primes_sieve, is_prime
from math import sqrt



def is_sum_of_a_prime_and_twice_a_square(number):
    return len([i for i in primes_sieve(number - 2) if sqrt((number - i)/2.0).is_integer()]) > 0

c = 7

while True:
    
    c = c + 2 
    
    if is_prime(c):
        continue
    
    if not is_sum_of_a_prime_and_twice_a_square(c):
        exit
    
print c


#sqrt((number - i)/2)

#[2, 3, 5, 7]