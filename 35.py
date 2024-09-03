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

def rotate(n):
    lastDigit = n % 10
    n = int(n/10)
    order = 1
    while order <= n:
        order *= 10
    return lastDigit * order + n

def isCircular(p):
    r = rotate(p)
    while r != p:
        if r % 2 == 0:
            return False
        else:
            for x in primes:
                if x > r:
                    return False
                elif x == r:
                    break
        r = rotate(r)
    return True



import time
t = time.time()
expandPrimesUpToN(1000000)
print("primes generation {:.5f}s".format(time.time()-t))

t = time.time()
circular = 0
for p in primes:
    if isCircular(p):
        circular += 1
print("circular counting {:.5f}s".format(time.time()-t))
print(circular)
