primes = [2,3,5,7,11]

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

def expandNextPrime():
    lastOdd = primes[-1] + 2
    primeCount = len(primes)
    while primeCount == len(primes):
        verifyPrime(lastOdd)
        lastOdd += 2

def truncateRight(n):
    return int(n/10)

def truncateLeft(n):
    order = 1
    while n > 10 * order:
        order *= 10
    return n % order


def testProperty(n):
    lastDigit = n % 10
    if lastDigit == 1 or lastDigit % 2 == 0:
        return False
    tl = truncateLeft(n)
    while tl > 0:
        if tl not in primes:
            return False
        tl = truncateLeft(tl)
    tr = truncateRight(n)
    while tr > 0:
        if tr not in primes:
            return False
        tr = truncateRight(tr)
    return True

found = []
while len(found) < 11:
    p = primes[-1]
    if testProperty(p):
        found.append(p)
        print(p)
    expandNextPrime()

print(sum(found), found)

