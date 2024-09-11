def countSums(n, primes, maxPrimeIndex):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        pid = maxPrimeIndex
        while pid >= 0:
            newN = n - primes[pid]
            total += countSums(newN, primes, pid)
            pid -= 1
        return total

from primes import primesSieve
import time
n = 20
t = time.time()
primes = primesSieve(1000)
while True:
    count = countSums(n, primes, len(primes)-1)
    if count > 5000:
        print(n, count, time.time()-t)
        break
    n += 1
