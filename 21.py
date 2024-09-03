def findSumOfDivisors(n):
    divisors = [1]
    potentialDivisor = 2
    while potentialDivisor * potentialDivisor <= n:
        if n % potentialDivisor == 0:
            divisors.append(potentialDivisor)
            if potentialDivisor * potentialDivisor != n:
                divisors.append(int(n/potentialDivisor))
        potentialDivisor += 1

    sum = 0
    for i in divisors:
        sum += i
    return sum


max_value = 0 # some amicable numbers might be below 10000 but their pair is above
dfun = [0]
for n in range(1,10000):
    dfun.append(findSumOfDivisors(n))
    if max_value < dfun[n]:
        max_value = dfun[n]
for n in range(10000,max_value+1):
    dfun.append(findSumOfDivisors(n))


amiSum = 0
for n in range(1,10000):
    if dfun[n] != n and n == dfun[dfun[n]]:
        amiSum += dfun[n]
        
print(amiSum)
