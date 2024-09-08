def distinctPrimes(n, primes):
    distinct = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            n = n // p
            distinct.append(p)
    return (n, distinct)

def totient(n, primes, potentialPrime):
    if potentialPrime and bSearch(n, primes):
        return n - 1
    t, distinct = distinctPrimes(n, primes)
    for p in distinct:
        t *= (p - 1)
    return t

from primes import primesSieve, bSearch
import time

maxD = 10**6
primes = primesSieve(maxD)
count = 0

odd = False
t = time.time()
for d in range(2, maxD+1):
    if d % (100000) == 0:
        print(d,"/",maxD, "t =", time.time() - t)
        t = time.time()
    count += totient(d, primes, odd and d % 10 not in [0,5])
    odd = not odd
print(count)
