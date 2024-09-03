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


def primeFactorsOf(n):
    expandPrimesUpToN(n)
    factors = []
    for i in primes:
        if i > n:
            break
        while n % i == 0:
            factors.append(i)
            n = int(n/i)
    return factors

def countUnique(arr):
    # arr is already sorted
    result = 1
    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i+1]:
            result += 1
    return result



for problemSize in [2,3,4]:
    found = []
    index = 3
    while True:
        if countUnique(primeFactorsOf(index)) == problemSize:
            found.append(index)
        else:
            found = []
        if len(found) == problemSize:
            print(found)
            break
        index += 1

