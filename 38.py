def splitIntoDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    return digits

def isPandigital(digits):
    digits = digits[:]
    digits.sort()
    for i in range(0,len(digits)):
        if digits[i] != i+1:
            return False
    return True

def restoreNumber(digits):
    n = 0
    for i in digits:
        n = 10*n + i
    return n


highest = 0
for n in range(1, 50000):
    index = 1
    candidate = []
    while len(candidate) < 9:
        candidate += splitIntoDigits(n * index)
        index += 1
    if len(candidate) == 9 and isPandigital(candidate):
            restored = restoreNumber(candidate)
            if restored > highest:
                highest = restored
                print(restored, n)

print(highest)

