def splitIntoDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = int(n/10)
    return digits


found = []
for d in range(11,99):
    for n in range (11, d):
        if d % 10 != 0 and n % 10 != 0:
            dDigits = splitIntoDigits(d)
            nDigits = splitIntoDigits(n)
            common = None
            if dDigits[0] in nDigits:
                common = dDigits[0]
            elif dDigits[1] in nDigits:
                common = dDigits[1]
            if common:
                dDigits.remove(common)
                nDigits.remove(common)
                if n * dDigits[0] == d * nDigits[0]:
                    found.append((nDigits[0], dDigits[0]))

print(found)
                
