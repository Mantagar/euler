from continuedFractions import approx
e = [2,1]
for i in range(1, 34):
    e += [i*2,1,1]
n,_ = approx(e[:100])

total = 0
while n > 0:
    total += n % 10
    n = n // 10
print(total)
