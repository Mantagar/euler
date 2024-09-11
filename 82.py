with open("inputs/82_input.txt") as inputFile:
    data = inputFile.read()
data = data.split('\n')
data = [[int(num) for num in line.split(',')] for line in data]

def visit(data, x, y):
    minValue = data[y][x+1]
    upWalk = 0
    for yw in range(y-1,-1,-1):
        upWalk += data[yw][x]
        value = upWalk + data[yw][x+1]
        if value < minValue:
            minValue = value
    downWalk = 0
    for yw in range(y+1,len(data)):
        downWalk += data[yw][x]
        value = downWalk + data[yw][x+1]
        if value < minValue:
            minValue = value
    return minValue

def traverseColumns(data):
    for x in range(len(data)-2,-1,-1):
        minValues = [visit(data, x, y) for y in range(len(data))]
        for y in range(len(data)):
            data[y][x] += minValues[y]

traverseColumns(data)
print(min([data[i][0] for i in range(len(data))]))
