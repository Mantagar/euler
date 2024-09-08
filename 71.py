def compare(a, b):
    left = a[0] * b[1]
    right = a[1] * b[0]
    if left == right:
        return 0
    elif left < right:
        return -1
    else:
        return 1


maxD = 10**6
target = (3, 7)
nearest = (0, 1)
n = maxD
d = maxD
while d > 1:
    while compare((n, d), target) == 1:
        n -= 1
    while compare((n, d), target) == -1:
        n += 1
    n -= 1
    if compare((n,d), nearest) == 1:
        nearest = (n,d)
    d -= 1

print(nearest)

