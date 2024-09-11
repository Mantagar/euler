def properPrimeFactorsOf(n, primes):
    f = []
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            f.append(p)
    return f
        


from primes import primesSieve

size = 12000
primes = primesSieve(size)
factors = [properPrimeFactorsOf(n, primes) for n in range(size+1)]

count = 0
for d in range(2,size+1):
    for n in range(1,d):
        if d < 3 * n and 2 * n < d:
            coprime = True
            for f in factors[n]:
                if f in factors[d]:
                    coprime = False
                    break
            if coprime:
                count += 1
print(count)




