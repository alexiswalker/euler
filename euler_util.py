def primes_sieve(limit):
    primes = [True]*limit
    primes[0] = primes[1] = False
    
    for(i, is_prime) in enumerate(primes):
        if is_prime:
            yield i 
            for n in range(i*i, limit,i):
                primes[n] = False

def is_prime(n):
    #return not any([n%i==0 for i in range(2,n)])
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

def rotate(string, n):
    return string[n:] + string[:n]

if __name__ == '__main__':
    for i in primes_sieve(100):
        print i 
