twos = 1
limit = 10**10
for _ in range(7830457):
    twos *= 2
    if twos > limit:
        twos -= limit
twos = 28433 * twos + 1
print(str(twos)[-10:])
