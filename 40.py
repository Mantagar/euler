def splitIntoDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    return digits


def findResult():
    result = 1
    index = 2
    counter = 2
    while True:
        for d in splitIntoDigits(index):
            if counter in [10, 100, 1000, 10000, 100000, 1000000]:
                result *= d
                if counter == 1000000:
                    return result
            counter += 1
        index += 1

print(findResult())
