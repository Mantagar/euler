count = 0
# minimum number of digits gained with each power is (numberOfDigits - 1), so only 1 to 9 need to be looked at
# once the number of digits and exponent mismatch they will never match again it
for i in range(1,10):
    n = 1
    d = len(str(i))
    while d == n:
        count += 1
        n += 1
        d = len(str(i**n)) 
print(count)
