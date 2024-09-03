def primesSieve(n):
    sieve = list(range(2, n+1))
    primes = []
    while len(sieve) > 0:
        p = sieve[0]
        primes.append(p)
        nextSieve = []
        multipliedSieve = [p*i for i in sieve]
        sIndex = 1
        msIndex = 0
        while sIndex < len(sieve):
            potentialP = sieve[sIndex]
            while potentialP > multipliedSieve[msIndex]:
                msIndex += 1
            if potentialP != multipliedSieve[msIndex]:
                nextSieve.append(potentialP)
            sIndex += 1
        sieve = nextSieve
    return primes


def primesNaive(n):
    primes = [2]
    i = 3
    while i <= n:
        isPrime = True
        for p in primes[1:]:
            if i % p == 0:
                isPrime = False
                break
            elif p*p >= i:
                break
        if isPrime:
            primes.append(i)
        i += 2
    return primes

def primesSkip3(n):
    primes = [2,3]
    skips = [2,4]
    s = 0
    i = 5
    while i <= n:
        isPrime = True
        for p in primes[1:]:
            if i % p == 0:
                isPrime = False
                break
            elif p*p >= i:
                break
        if isPrime:
            primes.append(i)
        i += skips[s]
        s = (s+1) % len(skips)
    return primes

def generateSkips(startingPrimes):
    limit = 1
    for i in startingPrimes:
        limit *= i
    offsets = list(range(3,limit+2,2))
    # find primes relative to the startingPrimes
    coprimes = []
    for i in offsets:
        isCoprime = True
        for p in startingPrimes:
            if i % p == 0:
                isCoprime = False
                break
        if isCoprime:
            coprimes.append(i)
    skips = []
    for i in range(0,len(coprimes)-1):
        skips.append(coprimes[i+1]-coprimes[i])
    skips.append(coprimes[0] - coprimes[-1] + limit)
    return skips

def primesSkip(n, startingPrimes=[2,3,5,7,11,13,17]):
    primes = startingPrimes
    skips = generateSkips(startingPrimes)
    s = 0
    i = skips[-1] + 1
    while i <= n:
        isPrime = True
        for p in primes[1:]:
            if i % p == 0:
                isPrime = False
                break
            elif p*p >= i:
                break
        if isPrime:
            primes.append(i)
        i += skips[s]
        s = (s+1) % len(skips)
    return primes

def bSearch(n, data):
    # basic binary search
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == n:
            return True
        if data[middle] < n:
            left = middle + 1
        else:
            right = middle - 1
    return False

def testComplexity():
    import time
    n = 1000000

    # terrible
    #t = time.time()
    #p = primesSieve(n)
    #t = time.time() - t
    #print("Sieve:", t, len(p))

    #t = time.time()
    #p = primesNaive(n)
    #t = time.time() - t
    #print("Naive:", t, len(p))

    #t = time.time()
    #p = primesSkip3(n)
    #t = time.time() - t
    #print("Skip 3:", t, len(p))

    # it slows after 17
    startingPrimes = [2,3,5,7,11,13,17]
    for i in range(0,len(startingPrimes)):
        t = time.time()
        p = primesSkip(n, startingPrimes[:i+1])
        t = time.time() - t
        print("Skip {}:".format(startingPrimes[i]), t, len(p), startingPrimes[:i+1])

    """
    Skip 2: 39.9777135848999 78498 [2]
    Skip 3: 26.891463041305542 78498 [2, 3]
    Skip 5: 21.625972509384155 78498 [2, 3, 5]
    Skip 7: 18.59758973121643 78498 [2, 3, 5, 7]
    Skip 11: 16.970937967300415 78498 [2, 3, 5, 7, 11]
    Skip 13: 16.122613191604614 78498 [2, 3, 5, 7, 11, 13]
    Skip 17: 15.286912202835083 78498 [2, 3, 5, 7, 11, 13, 17]
    """
