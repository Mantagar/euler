def splitNumberIntoDigits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = int(number / 10)
    return digits

def isPalindrome(number):
    digits = splitNumberIntoDigits(number)
    answer = True
    for i in range(0, int(len(digits)/2)):
        if digits[i] != digits[-i-1]:
            answer = False
            break
    return answer

a = 999
b = 999
while True:
    number = a * b
    if isPalindrome(number):
        print(number, a, b)
        break
    b -= 1
    if b < 900:
        a -= 1
        b = a

