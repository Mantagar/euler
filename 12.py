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
    while lastOdd < n:
        verifyPrime(lastOdd)
        lastOdd += 2

# NOTE giving up on primes, leaving for future use

def findNumberOfDivisors(n):
    divisors = 0
    highestDivisor = n
    potentialDivisor = 1
    while potentialDivisor < highestDivisor:
        if n % potentialDivisor == 0:
            highestDivisor = int(n / potentialDivisor)
            if highestDivisor == potentialDivisor:
                divisors += 1
            else:
                divisors += 2
        potentialDivisor += 1
    return divisors



def checkTriangleNumbers():
    divisors = 0
    numberNo = 0
    triangleSum = 0
    while divisors <= 500:
        numberNo += 1
        triangleSum += numberNo
        divisors = findNumberOfDivisors(triangleSum)
        print("divisors({}) sum({}) no({})".format(divisors, triangleSum, numberNo))


checkTriangleNumbers()
