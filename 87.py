from primes import primesSieve
import math

limit = 50 * 10**6
primes = primesSieve(int(math.sqrt(limit))+100)

found = [False] * limit
a = -1
while True:
    a += 1
    aExp = primes[a] ** 4
    if aExp >= limit:
        break
    b = -1
    while True:
        b += 1
        bExp = primes[b] ** 3
        abSum = aExp + bExp
        if abSum >= limit:
            break
        c = - 1
        while True:
            c += 1
            cExp = primes[c] ** 2
            abcSum = abSum + cExp
            if abcSum >= limit:
                break
            found[abcSum] = True

count = 0
for i in found:
    if i:
        count += 1
print(count)
