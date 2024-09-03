
def addAndExpand(left, right):
    digits = []
    for i in range(0,len(right)):
        digits.append(left[i] + right[i])
    for i in range(len(right),len(left)):
        digits.append(left[i])

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
    return digits

left = [1]
right = [1]
index = 2
while True:
    index += 1
    swap = addAndExpand(left, right)
    right = left
    left = swap
    if len(left) == 1000:
        print(index)
        break

