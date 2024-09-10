with open("inputs/99_input.txt") as inputFile:
    data = inputFile.read()
data = data.split('\n')

import math
bestLine = 0
bestValue = 0
for i in range(len(data)):
    base,exp = data[i].split(',')
    value = int(exp) * math.log(int(base))
    if value > bestValue:
        bestValue = value
        bestLine = i
print(bestLine + 1)
