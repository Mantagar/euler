from digits import digitsOf

def mul(digits, n):
    digits = digits[:]
    base = 10
    over = 0
    for i in range(1,len(digits)+1):
        digits[-i] = digits[-i] * n + over
        over = digits[-i] // base
        digits[-i] %= base
    while over > 0:
        digits = [over % base] + digits
        over = over // base
    return digits

def multiplyAndCompareDigits(digits, m):
    multipliedDigits = mul(digits, m)
    if len(multipliedDigits) != len(digits):
        return False
    sortedDigits = digits[:]
    sortedDigits.sort()
    multipliedDigits.sort()
    return sortedDigits == multipliedDigits
        

for i in range(10**5,2*10**5):
    digits = digitsOf(i)
    found = True
    for m in range(2,7):
        if not multiplyAndCompareDigits(digits, m):
            found = False
            break
    if found:
        print(i)
        break
