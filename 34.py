def digitsOf(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    return digits

def factorialOf(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f


def curiousSumOf(n):
    total = 0
    for i in digitsOf(n):
        total += factorialOf(i)
    return total

found = []
maxDigitFactorial = factorialOf(9)
index = 3
digits = digitsOf(index)
while 10**len(digits) <= maxDigitFactorial*len(digits):
    if index % 100000 == 0:
        print("Index:", index, found)
    if curiousSumOf(index) == index:
        found.append(index)
    index += 1
    digits = digitsOf(index)
print(sum(found))
