primes = [2,3,5,7,11,13,17]

def genPandigital(digits):
    if len(digits) == 0:
        yield []
    else:
        for i in range(0, len(digits)):
            nextDigits = digits[:i] + digits[i+1:]
            for variant in genPandigital(nextDigits):
                yield [digits[i]] + variant

def restoreNumber(digits):
    n = 0
    for i in digits:
        n = 10*n + i
    return n

def testProperty(digits):
    for p in range(0,len(primes)):
        if restoreNumber(i[p+1:p+4]) % primes[p] != 0:
            return False
    return True


digits = [9,8,7,6,5,4,3,2,1,0]
sum = 0
for i in genPandigital(digits):
    if i[0] != 0 and testProperty(i):
        sum += restoreNumber(i)

print(sum)
