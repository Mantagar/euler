factorial = [1]*10
for i in range(1,10):
    factorial[i] = factorial[i-1] * i

limit = factorial[9]*6
chain = [False] * (limit + 1)

def nextInChain(n):
    value = 0
    for d in str(n):
        value += factorial[int(d)]
    return value

def traverse(n):
    if chain[n]:
        return chain[n][1]
    else:
        idx = nextInChain(n)
        length = 1 if idx == n else traverse(idx) + 1
        chain[n] = (idx, length)
        return length

chain[145] = (145,1)
chain[169] = (363601,3)
chain[363601] = (1454,3)
chain[1454] = (169,3)
chain[871] = (45361,2)
chain[45361] = (871,2)
chain[872] = (45362,2)
chain[45362] = (872,2)

count = 0
for i in range(0,10**6):
    if not chain[i]:
        if traverse(i) == 60:
            print(i, chain[i])
            count += 1
print(count)
