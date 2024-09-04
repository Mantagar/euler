from digits import digitsOf, isPalindrome, addDigits

def isLychrel(n):
    index = 1
    digits = digitsOf(n)
    while index < 50:
        rev = digits[:]
        rev.reverse()
        added = addDigits(digits, rev)
        if isPalindrome(added):
            return False
        digits = added
        index += 1
    return True

def isLychrelStr(n):
    index = 1
    dig = str(n)
    rev = dig[::-1]
    while index < 50:
        dig = str(int(dig) + int(rev))
        rev = dig[::-1]
        if dig == rev:
            return False
        index += 1
    return True


# NOTE string operations are more efficient by far, restrain from using digits module
import time
t = time.time()
count = 0
for i in range(1,10**4):
    if isLychrel(i):
        count += 1
t = time.time() - t
print("Arrays:", count, t)

t = time.time()
count = 0
for i in range(1,10**4):
    if isLychrelStr(i):
        count += 1
t = time.time() - t
print("Strings:", count, t)
