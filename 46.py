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

def testNumber(comp):
    for p in primes:
        n = 1
        s = p + 2*n*n
        while comp > s:
            n += 1
            s = p + 2*n*n
        if comp == s:
            print("{} = {} + 2 x {}^2 = {}".format(comp, p, n, s))
            return True
    return False

comp = 3
while True:
    expandPrimesUpToN(comp)
    if comp != primes[-1] and not testNumber(comp):
        print(comp)
        break
    comp += 2
