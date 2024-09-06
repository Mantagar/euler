from continuedFractions import period
count = 0
for i in range(2,10001):
    _,p = period(i)
    if p % 2 == 1:
        count += 1
print(count)

