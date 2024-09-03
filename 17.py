wordLen = {
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten",
        11:"eleven",
        12:"twelve",
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eighteen",
        19:"nineteen",
        20:"twenty",
        30:"thirty",
        40:"forty",
        50:"fifty",
        60:"sixty",
        70:"seventy",
        80:"eighty",
        90:"ninety",
        100:"hundred",
        1000:"thousand"
    }

for k,v in wordLen.items():
    wordLen[k] = len(wordLen[k])

lettersUntil100 = 0
# 1 to 99
for i in range(1,100):
    if i<20:
        lettersUntil100 += wordLen[i]
    else:
        first = int(i/10) * 10
        second = i % 10
        lettersUntil100 += wordLen[first]
        if second != 0:
            lettersUntil100 += wordLen[second]
letters = lettersUntil100
for i in range(1,10):
    # hundreds without 'and'
    letters += wordLen[100] + wordLen[i]
    # hundreds with 'and'
    letters += (wordLen[100] + wordLen[i] + 3) * 99 + lettersUntil100
letters += wordLen[1000] + wordLen[1]

print(lettersUntil100)
print(letters)

# NOTE I forgot to add lettersUntil100 to the final sum so another approach was done to find the bug
def convertNumberToWord(n):
    first = int(n/1000)
    second = int(n/100)%10
    third = n%100
    length = 0
    if first > 0:
        length += wordLen[first] + wordLen[1000]
    if second > 0:
        length += wordLen[second] + wordLen[100]
        if third > 0:
            length += 3
    if third > 0:
        if third in wordLen:
            length += wordLen[third]
        else:
            length += wordLen[int(third/10)*10]
            if third%10!=0:
                length += wordLen[third%10]
    return length

anotherCount = 0
for i in range(1,100):
    anotherCount += convertNumberToWord(i)
print(anotherCount)

anotherCount = 0
for i in range(1,1001):
    anotherCount += convertNumberToWord(i)
print(anotherCount)
