with open("inputs/96_input.txt") as inputFile:
    data = inputFile.read()
data = data.split("\nGrid")
data = [d.split('\n', 1)[1] for d in data]

from sudoku import Sudoku

result = 0
for d in data:
    s = Sudoku(d)
    if not s.solve():
        print("Failed to solve")
        s.print()
    else:
        result += s.board[0][0] * 100 + s.board[0][1] * 10 + s.board[0][2]
print(result)
