x = 600851475143
prime = 1
while x != 1:
    prime += 2
    while x % prime == 0:
        x /= prime
print(prime)
