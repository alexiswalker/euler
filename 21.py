
n = 220 

def sum_divisors(n):
    return sum([x for x in range(1, n) if float(n)/x==n/x])

def are_amicable(n):
    s = sum_divisors(n)
    m = sum_divisors(s)
    
    return m==n and n!=s

r = []
for i in range(1,10000):
    if are_amicable(i):
        r.append(i)

print sum(r)