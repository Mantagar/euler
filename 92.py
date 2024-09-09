def chain(number, history):
    n = number
    visited = []
    while True:
        h = history[n]
        if h != 0:
            for v in visited:
                history[v] = h
            return h
        visited.append(n)
        newN = 0
        for d in str(n):
            newN += int(d) ** 2
        n = newN

count = 0
maxN = 10**7
history = [0]*maxN
history[89] = 89
history[1] = 1

import time
t = time.time()
for i in range(maxN-1, 0, -1):
    if chain(i, history) == 89:
        count += 1

print(count, time.time() - t)
