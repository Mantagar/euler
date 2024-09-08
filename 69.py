def distinctPrimes(n, primes):
    distinct = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            n = n // p
            distinct.append(p)
    return (n, distinct)

def nTotientRatio(n, primes, potentialPrime):
    if potentialPrime and bSearch(n, primes):
        return n / (n - 1)
    _, distinct = distinctPrimes(n, primes)
    n = 1
    d = 1
    for p in distinct:
        n *= p
        d *= (p - 1)
    return n/d

from primes import primesSieve, bSearch
import time

n = 10**6
primes = primesSieve(n)
highestValue = 0
bestN = 0

odd = False
t = time.time()
for i in range(2, n+1):
    if i % (100000) == 0:
        print(i,"/",n, "t =", time.time() - t)
        t = time.time()
    value = nTotientRatio(i, primes, odd and i % 10 not in [0,5])
    if value > highestValue:
        highestValue = value
        bestN = i
    odd = not odd
print(bestN)
