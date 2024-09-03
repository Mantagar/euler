def verifyPrime(primes, n):
    isPrime = True
    for p in primes[1:]:
        if p*p > n:
            break
        if n % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(n)


def findSumOfPrimes(n):
    primes = [2,3]
    odd = 5
    while odd <= n:
        verifyPrime(primes, odd)
        verifyPrime(primes, odd+2)
        odd += 6
    
    sum = 0
    for i in primes:
        if i <= n:
            sum += i
    print(sum)

findSumOfPrimes(10)
findSumOfPrimes(2000000)
