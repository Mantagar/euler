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

def longestChain(p, bestChain):
    start = 0
    end = 0
    sum = 0
    while True:
        if primes[start]*bestChain>p:
            return 0 
        sum += primes[end]
        end += 1
        while sum > p:
            sum -= primes[start]
            start += 1
        if sum == p:
            return end - start

bestPrime = 0
bestChain = 0
while primes[-1] < 1000000:
    p = primes[-1]
    chain = longestChain(p, bestChain)
    if chain > bestChain:
        bestPrime = p
        bestChain = chain
        print(bestPrime, bestChain)
    expandNextPrime()
