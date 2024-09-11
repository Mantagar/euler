def countRects(width, height):
    count = 0
    for w in range(1,width+1):
        for h in range(1,height+1):
            xOffsets = width - w + 1
            yOffsets = height - h + 1
            count += xOffsets * yOffsets
    return count


target = 2000000
nearestDiff = 999999
nearestW = 0
nearestH = 0

w = 1
h = 1
while countRects(w,h) < target:
    w += 1
while h <= w:
    count = countRects(w,h)
    diff = abs(target - count)
    if diff < nearestDiff:
        nearestDiff = diff
        nearestW = w
        nearestH = h

    w -= 1
    count = countRects(w,h)
    diff = abs(target - count)
    if diff < nearestDiff:
        nearestDiff = diff
        nearestW = w
        nearestH = h
    
    h += 1
    while countRects(w,h) > target:
        w -= 1
    w += 1

print(nearestW * nearestH, nearestW, nearestH)
