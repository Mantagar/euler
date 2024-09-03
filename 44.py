import math
def isPen(n):
    d = math.sqrt(1 + 24*n)
    return int(d) == d and (int(d) + 1) % 6 == 0


split = 1
while True:
    for n in range(1, split+1):
        sub = int((3*split*split+split*(6*n-1))/2)
        add = sub + int(3*n*n-n)
        if isPen(sub) and isPen(add):
            print("D({}) n1({}) n2({})".format(sub, n+split, n))
            exit()
    split += 1
