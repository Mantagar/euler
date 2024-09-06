def period(n):
    a = 1
    while a*a < n:
        a += 1
    a -= 1
    if a*a == n:
        return 0
    b = 1
    p = a
    cont = [(p,a,b)]
    while True:
        b = (n - a*a) // b
        p = 0
        while a*a < n:
            a -= b
            p += 1
        a += b
        p -= 1
        a = -a
        uniq = (p,a,b)
        if uniq in cont:
            periodLength = len(cont) - cont.index(uniq)
            continuedFraction = [t[0] for t in cont]
            return (continuedFraction, periodLength)
        else:
            cont.append(uniq)

def gcd(a,b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def approx(fraction, current=0):
    if current == len(fraction) - 1:
        return (fraction[-1],1)
    else:
        d,n = approx(fraction, current+1)
        n += fraction[current] * d
        common = gcd(n,d)
        return (n//common, d//common)
