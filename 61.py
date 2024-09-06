def getPolygonalType(n):
    types = []
    for t in range(2,8):
        inc = t
        gen = 1
        while gen < n:
            gen += inc
            inc += t - 1
        if gen == n:
            types.append(t + 1)
    return types

print("Calculating polygonal types for 4-digit numbers...")
cachedTypes = [[]]*1000 + [getPolygonalType(n) for n in range(1000,10000)]
validNumbers = [n for n in range(10000) if cachedTypes[n] != []]
print("Valid numbers:", len(validNumbers))

def findSet(maxType):
    if maxType <= 3:
        for i in validNumbers:
            yield [i]
    else:
        for smallerSet in findSet(maxType - 1):
            types = [cachedTypes[n] for n in smallerSet]
            end = smallerSet[-1] % 100
            if end >= 10:
                onlyValid = [n for n in validNumbers if cachedTypes[n] not in types and str(n)[:2] == str(end)]
                for i in onlyValid: 
                    yield smallerSet + [i]

maxType = 8
for found in findSet(maxType):
    if len(found) == maxType - 2 and str(found[0])[:2] == str(found[-1])[-2:]:
        print("Types", [cachedTypes[k] for k in found])
        print("Found", found)
        print("Sum", sum(found))
