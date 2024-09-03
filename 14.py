def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz(n/2)
    else:
        return 2 + collatz((3*n+1)/2)

number = 1
seqLen = 0
while number<1000000:
    currentSeqLen = collatz(number)
    if currentSeqLen > seqLen:
        seqLen = currentSeqLen
        print("no({}) length({})".format(number, currentSeqLen))
    number += 1
