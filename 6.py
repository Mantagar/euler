
def dif(maxNum):
    sumOfSquares = 0
    sum = 0
    for i in range(1, maxNum + 1):
        sumOfSquares += i*i
        sum += i

    print(sum*sum - sumOfSquares)
dif(10)
dif(100)
