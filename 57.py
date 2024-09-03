def approx():
    n = 1
    d = 2
    
    while True:
        yield (n+d, d)
        tmp = n + 2*d
        n = d
        d = tmp

gen = approx()
count = 0
for i in range(1000):
    n,d = next(gen)
    if len(str(n)) > len(str(d)):
        count += 1
print(count)
