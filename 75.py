limit = 1500000 // 2
found = [[] for _ in range(limit + 1)]
for m in range(2, limit+1):
    for n in range(1, m):
        prod = m * (n + m)
        if prod > limit:
            break
        c = m*m + n*n
        wire = prod
        wireC = c
        while wire <= limit:
            if wireC not in found[wire]:
                found[wire].append(wireC)
            wire += prod
            wireC += c

print(sum([1 for i in found if len(i)==1]))
