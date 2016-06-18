from euler_util import divisors
from itertools import combinations_with_replacement

sum_of_two_abundant_numbers = 28123 + 1

abundants = [i for i in range(1, sum_of_two_abundant_numbers) if sum([j for j in divisors(i)]) > i]
#28123
combinations = combinations_with_replacement(abundants, 2)

numbers_sum_abundant = set([i for i in combinations_with_replacement(abundants, 2) if sum(i) < sum_of_two_abundant_numbers])

print sum(set(range(1, sum_of_two_abundant_numbers)).difference(numbers_sum_abundant))