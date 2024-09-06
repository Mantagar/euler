
permutations = 5
cubeCount = {}
i = 100
found = None
while not found:
    cube = i*i*i
    digits = list(str(cube))
    digits.sort()
    digits = str(digits)
    if digits in cubeCount:
        cubeCount[digits].append(i)
    else:
        cubeCount[digits] = [i]
    if len(cubeCount[digits]) == permutations:
        found = digits
    i += 1

s = min(cubeCount[digits])
print(s, s*s*s)
