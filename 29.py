def getPrimeRepr(n):
    index = 2
    divisors = []
    while n > 1:
        if n % index == 0:
            divisors.append(index)
            n = int(n / index)
        else:
            index += 1
    compact = []
    count = 1
    last = divisors[0]
    for i in range(1,len(divisors)):
        if last == divisors[i]:
            count += 1
        else:
            compact.append(last)
            compact.append(count)
            count = 1
            last = divisors[i]
    compact.append(last)
    compact.append(count)
    # repr is [prime1, exp1, ..., primeN, expN]    
    return compact

def genTerms(a, b):
    terms = []
    for xa in range(2,a+1):
        t = getPrimeRepr(xa)
        for xb in range(2,b+1):
            tx = t[:]
            for i in range(0, len(t), 2):
                tx[i+1] *= xb
            terms.append(tx)
    return terms

def countTerm(a, b):
    t = genTerms(a,b)
    uniqueTerms = []
    for left in t:
        if len(uniqueTerms) != 0 and len(uniqueTerms) % 1000 == 0:
            print("PROGRESS", (len(uniqueTerms))/len(t) * 100, "%")
        isUnique = True
        for right in uniqueTerms:
            if len(left) == len(right):
                identical = True
                for i in range(0,len(left)):
                    if left[i] != right[i]:
                        identical = False
                        break
                if identical:
                    isUnique = False
                    break
        if isUnique:
            uniqueTerms.append(left)
    return len(uniqueTerms)

print(countTerm(5,5))
print(countTerm(8,8))
print(countTerm(100,100))


