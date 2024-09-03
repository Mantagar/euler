def findNumbers():
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if a+b+c == 1000 and a*a + b*b == c*c:
                    print(a*b*c, a, b, c)
                    return

findNumbers()
