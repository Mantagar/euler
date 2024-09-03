maxorder = 0
for i in range(3,1000):
    n = i
    while n % 2 == 0:
        n = int(n / 2)
    while n % 5 == 0:
        n = int(n / 5)
    if n != 1:
        order = 1
        ten = 10
        while ten % n != 1:
            ten *= 10
            order += 1
        if maxorder < order:
            maxorder = order
            print(n, order)
