digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def genPerm(digits):
    if len(digits) == 1:
        yield digits
    else:
        for i in range(0, len(digits)):
            for permutation in genPerm(digits[:i] + digits[i+1:]):
                yield [digits[i]] + permutation

counter = 0
for i in genPerm(digits):
    counter += 1
    if counter == 1000000:
        print(''.join(i))
        break

