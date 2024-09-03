
maxSolutions = 0
bestP = 0


for p in range(2,1001):
    foundSolutions = 0
    for b in range(1, p - 1):
        a = int(p * (p - 2*b) / 2 / (p - b))
        c = p - a - b
        if 1 < a <= b < c and c*c == a*a + b*b:
            foundSolutions += 1
    if foundSolutions > maxSolutions:
        maxSolutions = foundSolutions
        bestP = p
        print(p, foundSolutions)

