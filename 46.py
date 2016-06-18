from euler_util import primes_sieve, is_prime, is_odd
from math import sqrt



def is_sum_of_a_prime_and_twice_a_square(number):
    return len([i for i in primes_sieve(number - 2) if sqrt((number - i)/2.0).is_integer()]) > 0

print [i for i in range(1, 10000) if is_odd(i) and not is_prime(i) and not is_sum_of_a_prime_and_twice_a_square(i)]

