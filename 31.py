#slow
def denominationSums(n, units):
    if n == 0:
        yield []
    else:
        for i in range(0,len(units)):
            nextUnits = units[i+1:]
            probedUnit = units[i]
            nextN = n - probedUnit
            nextSum = []
            while not nextN < 0:
                nextSum.append(units[i])
                for nextGen in denominationSums(nextN, nextUnits):
                    yield nextSum + nextGen
                nextN -= probedUnit

#fast
def justCount(n, units):
    count = 0
    if n == 0:
        count = 1
    else:
        for i in range(0,len(units)):
            nextUnits = units[i+1:]
            probedUnit = units[i]
            nextN = n - probedUnit
            while not nextN < 0:
                count += justCount(nextN, nextUnits)
                nextN -= probedUnit
    return count

units = [200, 100, 50, 20, 10, 5, 2, 1]
target = 200


import time
t = time.time()
fast = justCount(target, units)
t = time.time() - t
print(fast, t)


t = time.time()
allSums = []
for i in denominationSums(target, units):
    allSums.append(i)
t = time.time() - t
print(len(allSums), t)
