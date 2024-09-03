
def evenlyDivisible(highestNumber):
    divisors = [2]
    for i in range(3, highestNumber+1):
        potential = i
        for d in divisors:
            if potential % d == 0:
                potential = int(potential / d)
        if potential > 1:
            divisors.append(potential)

    product = 1
    for d in divisors:
        product *= d
    print(product)

evenlyDivisible(10)
evenlyDivisible(20)
