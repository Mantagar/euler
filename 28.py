
def findDiagonalSum(size):
    dim = 1
    n = 1
    digSum = 1
    while dim < size:
        spacing = dim + 1
        for i in range(0, 4):
            n += spacing
            digSum += n
        dim += 2
    return digSum

print(findDiagonalSum(5))
print(findDiagonalSum(1001))
