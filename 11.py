with open("inputs/11_input.txt") as inputFile:
    data = inputFile.read()

rows = data.split('\n')
numbers = [r.split(' ') for r in rows]
for r in range(0,len(numbers)):
    for c in range(0, len(numbers[r])):
        numbers[r][c] = int(numbers[r][c])
    print(numbers[r])

maxProduct = 0

for r in range(0,len(numbers)):
    for c in range(0, len(numbers[r])-3):
        product = numbers[r][c] * numbers[r][c+1] * numbers[r][c+2] * numbers[r][c+3]
        if product > maxProduct:
            maxProduct = product

for r in range(0,len(numbers)-3):
    for c in range(0, len(numbers[r])):
        product = numbers[r][c] * numbers[r+1][c] * numbers[r+2][c] * numbers[r+3][c]
        if product > maxProduct:
            maxProduct = product

for r in range(0,len(numbers)-3):
    for c in range(0, len(numbers[r])-3):
        product = numbers[r][c] * numbers[r+1][c+1] * numbers[r+2][c+2] * numbers[r+3][c+3]
        if product > maxProduct:
            maxProduct = product
        product = numbers[r+3][c] * numbers[r+2][c+1] * numbers[r+1][c+2] * numbers[r][c+3]
        if product > maxProduct:
            maxProduct = product

print(maxProduct)
