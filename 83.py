with open("inputs/83_input.txt") as inputFile:
    data = inputFile.read()
data = data.split('\n')
data = [[int(num) for num in line.split(',')] for line in data]

visited = [[False] * len(data) for _ in range(len(data))]
distance = [[999999999] * len(data) for _ in range(len(data))]
distance[len(data)-1][len(data)-1] = 0
def visit(y, x):
    if visited[y][x]:
        return []
    visited[y][x] = True
    nextNodes = []
    nodeWeight = distance[y][x] + data[y][x]
    if y > 0:
        if distance[y-1][x] > nodeWeight:
            distance[y-1][x] = nodeWeight
            nextNodes.append((y-1, x))
    if y < len(data) - 1:
        if distance[y+1][x] > nodeWeight:
            distance[y+1][x] = nodeWeight
            nextNodes.append((y+1, x))
    if x > 0:
        if distance[y][x-1] > nodeWeight:
            distance[y][x-1] = nodeWeight
            nextNodes.append((y, x-1))
    if x < len(data) - 1:
        if distance[y][x+1] > nodeWeight:
            distance[y][x+1] = nodeWeight
            nextNodes.append((y, x+1))
    return nextNodes

def dijkstra(startY, startX):
    nodes = [(startY, startX)]

    while len(nodes) > 0:
        # get minimal node
        y,x = nodes[0]
        minimalWeight = distance[y][x]
        minimalNode = nodes[0]
        for n in nodes:
            y,x = n
            weight = distance[y][x]
            if minimalWeight > weight:
                minimalWeight = weight
                minimalNode = n
        
        nodes.remove(minimalNode)
        nodes += visit(minimalNode[0], minimalNode[1])


dijkstra(len(data)-1, len(data)-1)
print(distance[0][0] + data[0][0])
