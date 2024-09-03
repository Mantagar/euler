import math
def isPen(n):
    d = math.sqrt(1 + 24*n)
    return int(d) == d and (int(d) + 1) % 6 == 0

def isTri(n):
    d = math.sqrt(8*n + 1)
    return d == int(d)

def isHex(n):
    d = math.sqrt(8*n + 1)
    return d == int(d) and (int(d)+1) % 4 == 0

calcHex = lambda n: n*(2*n-1)

i = 143
found = 0
while True:
    t = calcHex(i)
    if isPen(t) and isTri(t):
        print(t, i)
        found += 1
        if found == 2:
            break
    i+=1




