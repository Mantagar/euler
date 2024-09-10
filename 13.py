with open("inputs/13_input.txt") as inputFile:
    data = inputFile.read()

stringNums = data.split('\n')
digitSum = []
for i in range(0, 50):
    digitSum.append(0)
    for n in stringNums:
        digitSum[i] += int(n[i])

for i in range(1, 50):
    digitSum[-i-1] += int(digitSum[-i] / 10)
    digitSum[-i] = digitSum[-i] % 10

asString = ""
for i in range(0, 50):
    asString += str(digitSum[i])
print(asString)
print(asString[:10])

