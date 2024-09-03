
def multiplyAndExpand(digits, multiplier):
    for i in range(0,len(digits)):
        digits[i] *= multiplier

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

digits = [1]
for i in range(0,1000):
    multiplyAndExpand(digits, 2)

sum = 0
for i in digits:
    sum += i
print(sum)
