def primesSieve(n):
    # by far the fastest as it doesn't have dividing overhead
    # only odd numbers are considered
    # prime p needs to be incremented by 2 p times to get its multiples
    sieve = list(range(3, n+1, 2))
    primes = [2]
    index = 0
    jumpingIndex = 0
    while index < len(sieve):
        p = sieve[index]
        primes.append(p)
        jumpingIndex = index + p
        while jumpingIndex < len(sieve):
            sieve[jumpingIndex] = 0
            jumpingIndex += p
        index += 1
        while index < len(sieve) and sieve[index] == 0:
            index += 1
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
        s = (s+1) % len(skips)
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

    t = time.time()
    p = primesSieve(n)
    t = time.time() - t
    print("Sieve:", t, len(p))

    startingPrimes = [2,3,5,7,11,13,17]
    for i in range(0,len(startingPrimes)):
        t = time.time()
        p = primesSkip(n, startingPrimes[:i+1])
        t = time.time() - t
        print("Skip {}:".format(startingPrimes[i]), t, len(p), startingPrimes[:i+1])

    """
n = 10**7
Sieve: 1.9706051349639893 664579              <------ by far the best
Skip 2: 15.992695569992065 664579 [2]         <------ no gain for connsecutive skips (int limits?)
Skip 3: 15.685003757476807 664579 [2, 3]
Skip 5: 15.313693761825562 664579 [2, 3, 5]
Skip 7: 15.313390254974365 664579 [2, 3, 5, 7]
Skip 11: 15.109517812728882 664579 [2, 3, 5, 7, 11]
Skip 13: 14.996946096420288 664579 [2, 3, 5, 7, 11, 13]
Skip 17: 15.073673009872437 664579 [2, 3, 5, 7, 11, 13, 17]
    """
