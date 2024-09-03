def canBeWrittenAsSum(n, power):
    sum = n
    while n > 0:
        digit = n % 10
        sum -= digit ** power
        if sum < 0:
            break
        n = int(n / 10)
    return sum == 0

def getUpperLimit(power):
    nines = 9 ** power
    digitCount = 1
    while True:
        limit = nines * digitCount
        if limit < 10 ** digitCount:
            return limit
        digitCount += 1

def findAllWrittableAsSum(power):
    found = []
    for i in range(2,getUpperLimit(power)+1):
        if canBeWrittenAsSum(i, power):
            found.append(i)
    return found

size4 = findAllWrittableAsSum(4)
print(sum(size4), size4)

size5 = findAllWrittableAsSum(5)
print(sum(size5), size5)
