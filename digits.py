def digitsOf(n):
    return [int(c) for c in str(n)]


# NOTE don't use arrays of digits at all, simple strings are more efficient

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

def isPalindrome(digits):
    for i in range(0, len(digits)//2):
        if digits[i] != digits[-i-1]:
            return False
    return True

def addDigits(left, right):
    left = left[::-1]
    right = right[::-1]

    digitDiff = len(right) - len(left)
    if digitDiff > 0:
        left += [0] * digitDiff
    elif digitDiff < 0:
        right += [0] * (-digitDiff)

    for i in range(len(right)):
        left[i] += right[i]
    
    digits = left
    for i in range(0,len(digits)-1):
        while digits[i] > 9:
            digits[i+1] += int(digits[i] / 10)
            digits[i] = digits[i] % 10

    index = len(digits) - 1
    while digits[index] > 9:
        newDigit = int(digits[index] / 10)
        digits[index] = digits[index] % 10
        index += 1
        digits.append(newDigit)

    digits.reverse()
    return digits

