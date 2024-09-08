def totient(n, distinct):
    t = n
    for p in distinct:
        t *= (p - 1)
        t /= p
    return int(t)

from primes import primesSieve, bSearch
import math

maximumN = 10**7
primes = primesSieve(maximumN)

solution = [0, 10**6]

def testVariants(n, d, e1, e2, solution):
    i = n * d[0]**e1 * d[1]**e2
    if i >= maximumN:
        return
    t = totient(i, d)
    strI = str(i)
    strT = str(t)
    v = i/t
    if len(strI) == len(strT) and sorted(strI) == sorted(strT):
        print(i, v, d)
        solution[0] = i
        solution[1] = v
    testVariants(n, d, e1+1, e2, solution)
    testVariants(n, d, e1, e2+1, solution)


for lid in range(3, len(primes)):
    for rid in range(lid+1, len(primes)):
        lp = primes[lid]
        rp = primes[rid]
        i = lp * rp
        if i >= maximumN:
            break
        # v should be +1 but it doesn't matter while comparing and its 1 less operation
        v = lp * rp / (lp - 1) / (rp - 1)
        if v < solution[1]:
            d = [lp, rp]
            testVariants(i, d, 0, 0, solution)

print(solution)
