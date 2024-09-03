import itertools

primes = [2,3]
def verifyPrime(n):
    isPrime = True
    for p in primes[1:]:
        if p*p > n:
            break
        if n % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(n)

def expandPrimesUpToN(n):
    lastOdd = primes[-1]
    lastOdd += 2
    while lastOdd <= n:
        verifyPrime(lastOdd)
        lastOdd += 2

def nToDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    return digits

def digitsToN(digits):
    n = 0
    for i in digits:
        n = n*10 + i
    return n

expandPrimesUpToN(9999)
found = []
for i in range(1112, 9999):
    digits = nToDigits(i)
    if 0 not in digits:
        candidates = [digitsToN(perm) for perm in itertools.permutations(digits)]
        candidates.sort()
        for c in candidates:
            term1 = c + 3330
            term2 = term1 + 3330
            if term2 > candidates[-1]:
                break
            if term1 in candidates and term2 in candidates and c in primes and term1 in primes and term2 in primes:
                    f = (c,term1,term2)
                    if f not in found:
                        found.append(f)
                        break
        if len(found) == 2:
            print(found)
            break

digs = []
for i in found[1]:
    digs += nToDigits(i)
print(digitsToN(digs))
