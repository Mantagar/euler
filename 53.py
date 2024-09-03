def comb(n, r):
    up = 1
    down = 1
    for i in range(0,r):
        up *= (n - i)
        down *= (r - i)
    return up // down

def countSolutions(n):
    found = n + 1
    broke = False
    for r in range(n//2):
        if comb(n, r) <= 1000000:
            found -= 2
        else:
            broke = True
            break
    if not broke:
        if comb(n, n//2+1) <= 1000000:
            found -= 1
            if n % 2 == 1:
                found -= 1
    return found

count = 0
for i in range(1,101):
    count += countSolutions(i)

print(count)
