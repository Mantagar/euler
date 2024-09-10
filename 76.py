def countSums(n, maxElement):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        element = maxElement
        while element > 0:
            newN = n - element
            total += countSums(newN, element)
            element -= 1
        return total

import time
n = 100
t = time.time()
print(countSums(n, n-1), time.time()-t)
