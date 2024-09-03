def splitIntoDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    return digits

def isPandigital(digits):
    digits.sort()
    for i in range(0,len(digits)):
        if digits[i] != i+1:
            return False
    return True

found = []
for i in range(1000, 10000):
    div = 2
    while div*div < i:
        if i % div == 0:
            digits = splitIntoDigits(div) + splitIntoDigits(int(i/div)) + splitIntoDigits(i)
            if len(digits) == 9 and isPandigital(digits):
                found.append(i)
                break
        div += 1

print(sum(found), found)
