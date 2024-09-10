with open("inputs/42_input.txt") as inputFile:
    data = inputFile.read()
data = data.replace('\"',"").split(',')

import math
def isTriangle(n):
    d = math.sqrt(8*n + 1)
    return d == int(d)

def wordValue(word):
    s = 0
    for i in word:
        s += ord(i) - ord("A") + 1
    return s


count = 0
for word in data:
    if isTriangle(wordValue(word)):
        count += 1
print(count)

