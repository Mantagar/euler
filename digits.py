def digitsOf(n):
    return [int(c) for c in str(n)]

# slower and erroneous for huge numbers
# not looking into that
def digitsOfBase(n, base=10):
    digits = []
    while n > 0:
        digits.append(n%base)
        n //= base
    digits.reverse()
    return digits

def nFromDigits(digits, base=10):
    n = 0
    for i in digits:
        n = n*base + i
    return n
