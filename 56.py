from digits import digitsOf


best = 0
for a in range(1,100):
    for b in range(1,100):
        s = sum(digitsOf(a**b))
        if best < s:
            print(a,b,s)
            best = s


