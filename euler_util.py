def primes_sieve(limit):
    limit = limit + 1
    primes = [True]*limit
    primes[0] = primes[1] = False
    
    for(i, is_prime) in enumerate(primes):
        if is_prime:
            yield i 
            for n in range(i*i, limit,i):
                primes[n] = False

def is_prime(n):
    #return not any([n%i==0 for i in range(2,n)])
    if n < 2:
        return False
        
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

def rotate(string, n):
    return string[n:] + string[:n]

def divisors(number):
    for i in range(1, number/2+1):
        if number%i == 0:
            yield i

def is_odd(number):
    return number & 1 == 1

if __name__ == '__main__':
    print [i for i in range(3,14,2) if is_prime(i)]

