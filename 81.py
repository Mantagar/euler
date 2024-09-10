with open("inputs/81_input.txt") as inputFile:
    data = inputFile.read()
data = data.split('\n')
data = [[int(num) for num in line.split(',')] for line in data]

def traverse(data, now=1):
    if now >= len(data):
        return
    data[now][0] += data[now-1][0]
    data[0][now] += data[0][now-1]
    for i in range(1, now):
        data[now][i] += min(data[now-1][i],data[now][i-1])
        data[i][now] += min(data[i-1][now],data[i][now-1])
    data[now][now] += min(data[now-1][now],data[now][now-1])
    traverse(data, now + 1)

traverse(data)
print(data[-1][-1])
