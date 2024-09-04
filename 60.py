from primes import primesSieve, bSearch, nextPrime

primes = primesSieve(10**8)[1:]
def findSetOfPrimes(setSize):
    if setSize == 1:
        for i in primes:
            yield [i]
    for s in findSetOfPrimes(setSize-1):
        smallerSet = s
        lengths = [10**len(str(s)) for s in smallerSet]
        indices = list(range(len(smallerSet)))
        for p in primes[:primes.index(smallerSet[-1])]:
            valid = True
            pOffset = 10**len(str(p))
            for each in indices:
                concat = p*lengths[each] + smallerSet[each]
                while concat > primes[-1]:
                    additionalPrime = nextPrime(primes)
                    primes.append(additionalPrime)
                valid = bSearch(concat, primes)
                if not valid:
                    break
                concat = smallerSet[each]*pOffset + p
                while concat > primes[-1]:
                    additionalPrime = nextPrime(primes)
                    primes.append(additionalPrime)
                valid = bSearch(concat, primes)
                if not valid:
                    break
            if valid:
                yield smallerSet + [p]

for found in findSetOfPrimes(5):
    print(sum(found), found)
    break
