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


def canBeRepresented(abundant, n):
    for right in range(len(abundant) - 1, -1, -1):
        for left in range(0, right+1):
            sum = abundant[right] + abundant[left]
            if sum > n:
                break
            elif sum == n:
                return True
    return False

abundant = []
cases = []
for n in range(1,28124):
    if n % 1000 == 0:
        print(n)
    if findSumOfDivisors(n) > n:
        abundant.append(n)
    if not canBeRepresented(abundant, n):
        cases.append(n)

sum = 0
for i in cases:
    sum += i
print(sum)

