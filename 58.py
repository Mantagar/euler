from primes import primesSieve
import time

t = time.time()
primes = primesSieve(700000000)
t = time.time() - t
print("Primes generated in:",t)
p = 0

confirmed = 0
index = 1
layer = 1
diagNums = 1
while True:
    skip = layer * 2
    for _ in range(3):
        index += skip
        potentialPrime = index
        while primes[p] < potentialPrime:
            p += 1
        if primes[p] == potentialPrime:
            confirmed += 1
            p += 1
    # 4th diagonal contains squares
    index += skip
    
    diagNums += 4
    layer += 1
    ratio = confirmed/diagNums
    if layer % 1000 == 0:
        print("ratio({}) primes({}/{})".format(ratio, p, len(primes)))
    if ratio < .1:
        print(ratio)
        print(layer*2-1)
        exit()
