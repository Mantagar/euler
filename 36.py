def digitsOf(n, base):
    digits = []
    while n > 0:
        digits.append(n%base)
        n = int(n/base)
    return digits


def isPalindrome(digits):
    for i in range(0, int(len(digits)/2)):
        if digits[i] != digits[-i-1]:
            return False
    return True


s = 0
for i in range(1,1000000):
    if isPalindrome(digitsOf(i,10)) and isPalindrome(digitsOf(i,2)):
        s += i
print(s)
