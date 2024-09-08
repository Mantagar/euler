def nextPrime(primes):
    candidate = primes[-1] + 2
    while True:
        for p in primes:
            if p*p > candidate:
                return candidate
            if candidate % p == 0:
                break
        candidate += 2

def primesSieve(n):
    import time
    print("Prime sieve running...")
    t = time.time()
    # by far the fastest as it doesn't have dividing overhead
    # only odd numbers are considered (but it works also when fed table of natural numbers)
    sieve = list(range(3, n+1, 2))
    index = 0
    while True:
        
        zeroMultiplesOfPrime(sieve, index)

        # from index to index + p(p-1)/2 there are only primes and zeros
        if len(sieve) < index + (sieve[index] - 1)//2*sieve[index] + 2:
            break

        index += 1
        while sieve[index] == 0:
            index += 1

    primes = [2] + [p for p in sieve if p != 0]
    print("primes({}) {:.5f}s".format(len(primes), time.time() - t))
    return primes

def zeroMultiplesOfPrime(sieve, index):
    p = sieve[index]
    jumpingIndex = index + p
    while jumpingIndex < len(sieve):
        sieve[jumpingIndex] = 0
        jumpingIndex += p

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

def primesSkip(n, startingPrimes=[2,3,5,7]):
    # all the generated numbers will be coprime to startingPrimes
    primes = []
    skips = generateSkips(startingPrimes)
    s = 0
    i = skips[-1] + 1
    while i <= n:
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
                break
            elif p*p >= i:
                break
        if isPrime:
            primes.append(i)
        i += skips[s]
        s = s+1
        if s == len(skips):
            s -= len(skips)
    return startingPrimes + primes

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
    n = 10**7

    primesSieve(n)

    startingPrimes = [2,3,5,7,11,13,17]
    for i in range(0,len(startingPrimes)):
        t = time.time()
        p = primesSkip(n, startingPrimes[:i+1])
        t = time.time() - t
        print("Skip {}:".format(startingPrimes[i]), t, len(p), startingPrimes[:i+1])

    """
n = 10**7
Sieve: 1.9706051349639893 664579              <------ by far the best (no division overhead)
Skip 2: 15.992695569992065 664579 [2]         <------ almost no gain for connsecutive skips
Skip 3: 15.685003757476807 664579 [2, 3]
Skip 5: 15.313693761825562 664579 [2, 3, 5]
Skip 7: 15.313390254974365 664579 [2, 3, 5, 7]
Skip 11: 15.109517812728882 664579 [2, 3, 5, 7, 11]
Skip 13: 14.996946096420288 664579 [2, 3, 5, 7, 11, 13]
Skip 17: 15.073673009872437 664579 [2, 3, 5, 7, 11, 13, 17]
primes(664579) 1.41065s
Skip 2: 17.34155249595642 664579 [2]
Skip 3: 16.83974289894104 664579 [2, 3]
Skip 5: 16.516836404800415 664579 [2, 3, 5]
Skip 7: 16.274359703063965 664579 [2, 3, 5, 7]
Skip 11: 16.21398687362671 664579 [2, 3, 5, 7, 11]
Skip 13: 16.0749351978302 664579 [2, 3, 5, 7, 11, 13]
    """
