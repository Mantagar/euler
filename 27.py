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
    while lastOdd <= n:
        lastOdd += 2
        verifyPrime(lastOdd)

def expandNextPrime():
    originalCount = len(primes)
    offset = 2
    while len(primes) == originalCount:
        verifyPrime(primes[-1] + offset)
        offset += 2

def countConsPrimes(a, b):
    n = 1
    while True:
        p = n*n + a*n + b
        expandPrimesUpToN(p)
        if p not in primes:
            return n
        n += 1


index = 0
bestCount = 0
coeffProduct = 0
while True:
    while index + 1 > len(primes):
        expandNextPrime()
    b = primes[index]
    if b > 1000:
        break
    for a in range(-999,1000):
        # b needs to be a prime when n is 0
        count = countConsPrimes(a, b)
        if count > bestCount:
            bestCount = count
            print("a({}) b({}) primes({})".format(a, b, count))
            coeffProduct = a * b
    index += 1

print(coeffProduct)
    
