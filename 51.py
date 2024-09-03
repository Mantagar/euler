def nToDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    return digits

def digitsToN(digits):
    n = 0
    for i in digits:
        n = n*10 + i
    return n


import itertools
from primes import primesSkip, bSearch


family = 8
for order in range(1, 7):
    primes = primesSkip(10**order,[2,3,5,7,11,13])
    replacementWays = list(itertools.product([True,False], repeat=order))[1:-1]
    modded = [0] * order
    smallest = []
    for r in replacementWays:
        constPartsCounted = 0
        for i in r:
            if not i:
                constPartsCounted += 1
        end = 10 ** constPartsCounted
        start = end // 10
        for constPart in range(start,end):
            constDigits = nToDigits(constPart)
            constIndex = 0
            for i in range(len(r)):
                if not r[i]:
                    modded[i] = constDigits[constIndex]
                    constIndex += 1

            counter = 0
            found = []
            for rdig in range(10):
                if rdig == 0 and r[0]:
                    continue
                for i in range(order):
                    if r[i]:
                        modded[i] = rdig
                moddedNumber = digitsToN(modded)
                if bSearch(digitsToN(modded), primes):
                    counter += 1
                    found.append(moddedNumber)
            if counter == family:
                found.sort()
                if len(smallest) == 0 or smallest[0] > found[0]:
                    print(found, r)
                    smallest = found
    if len(smallest) != 0:
        break
