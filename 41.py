primes = [2,3,5,7]
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


def genPandigital(digits):
    if len(digits) == 0:
        yield []
    else:
        for i in range(0, len(digits)):
            nextDigits = digits[:i] + digits[i+1:]
            for variant in genPandigital(nextDigits):
                yield [digits[i]] + variant

def restoreNumber(digits):
    n = 0
    for i in digits:
        n = 10*n + i
    return n

def isPrime(n):
    for p in primes:
        if p*p > n:
            break
        if n % p == 0:
            return False
    return True




digits = [9,8,7,6,5,4,3,2,1]
import math
expandPrimesUpToN(math.sqrt(restoreNumber(digits)))
for start in range(0, 9):
    for i in genPandigital(digits[start:]):
        if i[-1] in [9,7,3,1] and sum(i) % 3 != 0:
            res = restoreNumber(i)
            if isPrime(res):
                print(res)
                break
