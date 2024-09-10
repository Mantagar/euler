with open("inputs/22_input.txt") as inputFile:
    data = inputFile.read()
data = data.split(',')
data = [entry[1:-1] for entry in data]
data.sort()

scores = 0
for i in range(0, len(data)):
    charScore = 0
    for letter in data[i]:
        charScore += ord(letter) - ord('A') + 1
    scores += charScore * (i + 1)
    if data[i] == 'COLIN':
        print(charScore*(i+1))

print(scores)

