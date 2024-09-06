def findMinimumX_tooSlow(d):
    # too slow
    reminders = []
    for r in range(d):
        reminders.append(r*r % d)
    ones = [r for r in range(len(reminders)) if reminders[r] == 1]
    # x^2 = 1 mod D only for r in "ones", x can only be of form k*d + r
    root = math.sqrt(d)
    rootInv = 1 / root
    baseX = 0
    while True:
        for offset in ones:
            x = baseX + offset
            y = max(2,int(x * rootInv))
            t = x*x - d*y*y
            # while will run 1 time if math.sqrt(d)**2 >= d and 2 timems otherwise
            while t >= 1:
                if t == 1:
                    return (x,y)
                t -= (2*y+1)*d
                y += 1
        baseX += d

def findMinimumX_stillTooSlow(d):
    reminders = []
    for n in range(d):
        reminders.append(n*n % d)
    reminders = [n for n in range(len(reminders)) if reminders[n] == 1]
    # x^2 = 1 mod D only for r, x can only be of form k*d + r
    # now the first y^2 found is our solution
    k = 0
    while True:
        part1 = d*k*k
        part2 = 2*k
        for r in reminders:
            ySquared = part1 + part2*r + (r*r-1)//d
            y = math.sqrt(ySquared)
            y = math.floor(y+.5)
            if y*y == ySquared and y != 0:
                return (d*k + r, y)
        k += 1

def findMinimumX_viaContinuedFractions(d):
    f,p = period(d)
    if p % 2 == 0:
        f = f[:-1]
    else:
        f = f + f[len(f)-p:-1]
    return approx(f)

from continuedFractions import period, approx
import math
import time

invalidD = [n*n for n in range(2,33)]
validD = [n for n in range(2,1001) if n not in invalidD]
maxX = 0
maxD = 0
for d in validD[::1]:
    t = time.time()
    #x,y = findMinimumX_tooSlow(d)
    #x,y = findMinimumX_stillTooSlow(d)
    x,y = findMinimumX_viaContinuedFractions(d)
    if x > maxX:
        print("x({}) D({}) y({}) {:.5f}".format(x, d, y, time.time()-t))
        maxX = x
        maxD = d
print(maxD)
