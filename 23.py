from euler_util import divisors
from itertools import combinations_with_replacement

sum_of_two_abundant_numbers = 28123 + 1

numbers = range(1, sum_of_two_abundant_numbers)

abundants = [i for i in numbers if sum([j for j in divisors(i)]) > i]

combinations = combinations_with_replacement(abundants, 2)

numbers_sum_abundant = set([sum(i) for i in combinations if sum(i) < sum_of_two_abundant_numbers])

print sum(set(numbers).difference(numbers_sum_abundant))