a = 1
b = 2
sum = 2
while True:
    c = a + b
    a = b + c
    b = a + c
    if b < 4000000:
        sum += b
    else:
        break
print(sum)
