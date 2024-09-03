def digitsOf(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    return digits

def nFromDigits(digits):
    n = 0
    for i in digits:
        n = n*10 + i
    return n
