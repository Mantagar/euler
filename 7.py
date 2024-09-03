def findNthPrime(n):
    primes = [2]
    odd = 3
    while len(primes) < n:
        isOddPrime = True
        for p in primes:
            if odd % p == 0:
                isOddPrime = False
                break
        if isOddPrime:
            primes.append(odd)
        odd += 2

    print(primes[-1])

findNthPrime(6)
findNthPrime(10001)
