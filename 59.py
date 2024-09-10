with open("inputs/59_input.txt") as inputFile:
    data = inputFile.read()
data = [int(entry) for entry in data.split(',')]

from digits import digitsOfBase, nFromDigits

def xor(n1, n2):
    x = n1[:] if type(n1) is list else digitsOfBase(n1,2)
    y = n2[:] if type(n2) is list else digitsOfBase(n2,2)
    offset = len(x) - len(y)
    if offset > 0:
        y = [0]*offset + y
    elif offset < 0:
        x = [0]*(-offset) + x
    for i in range(len(x)):
        x[i] = int(bool(x[i]) ^ bool(y[i]))
    return x


def decrypt(encrypted, password):
    decrypted = []
    i = 0
    p = 0
    while len(decrypted) < len(encrypted):
        decryptedDigits = xor(encrypted[i],password[p])
        decrypted.append(nFromDigits(decryptedDigits,2))
        p = (p + 1) % len(password)
        i += 1
    return decrypted

def text(intList):
    return "".join([chr(i) for i in intList])


for a in range(ord('a'),ord('z')+1):
    adigs = digitsOfBase(a,2)
    for b in range(ord('a'),ord('z')+1):
        bdigs = digitsOfBase(b,2)
        for c in range(ord('a'),ord('z')+1):
            cdigs = digitsOfBase(c,2)
            password = [adigs,bdigs,cdigs]
            decrypted = decrypt(data, password)
            if " the " in text(decrypted):
                print(text(decrypted))
                print(sum(decrypted))
                exit()
            

