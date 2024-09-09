def fill(n):
    if len(n) == 0:
        yield []
    else:
        for i in range(len(n)):
            for subFill in fill(n[:i]+n[i+1:]):
                result = subFill + [n[i]]
                if isValid(result):
                    yield result

def isValid(n):
    upTo = len(n)
    if upTo <= 6:
        return True
    v1 = n[0] + n[5] + n[6]
    if upTo == 7:
        # max line sum is floor(averageOfElems(n) * 3)
        return v1 < 17
    v2 = n[1] + n[6] + n[7]
    if upTo == 8:
        return v1 == v2
    v3 = n[2] + n[7] + n[8]
    if upTo == 9:
        return v1 == v2 == v3
    v4 = n[3] + n[8] + n[9]
    v5 = n[4] + n[9] + n[5]
    return v1 == v2 == v3 == v4 == v5

def genString(n):
    lowest = 0
    for i in range(1,5):
        if n[lowest] > n[i]:
            lowest = i
    v1 = str(n[0]) + str(n[5]) + str(n[6])
    v2 = str(n[1]) + str(n[6]) + str(n[7])
    v3 = str(n[2]) + str(n[7]) + str(n[8])
    v4 = str(n[3]) + str(n[8]) + str(n[9])
    v5 = str(n[4]) + str(n[9]) + str(n[5])
    lines = [v1,v2,v3,v4,v5]
    lines = lines[lowest:] + lines[:lowest]
    return ''.join(lines)

n = list(range(1,11))
best = ''
for i in fill(n):
    strI = genString(i)
    if strI > best:
        print(strI, i)
        best = strI
 
