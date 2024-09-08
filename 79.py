fragments = "319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716".split(' ')

def findFirstDigit():
    positions = {}
    for f in fragments:
        for i in range(len(f)):
            digit = f[i]
            if digit in positions:
                places = positions[digit]
                if i not in places:
                    places.append(i)
            else:
                positions[digit] = [i]
    
    return [k for k in positions.keys() if len(positions[k]) == 1 and positions[k][0] == 0]


password = ""
while True:
    d = findFirstDigit()
    if len(d) == 0:
        break
    d = d[0]
    newFragments = []
    for f in fragments[:]:
        if f[0] == d:
            if len(f) > 1:
                newFragments.append(f[1:])
        else:
            newFragments.append(f)
    fragments = newFragments
    password += d
    

print(password)

