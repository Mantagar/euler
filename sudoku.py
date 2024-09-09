class Sudoku:
    def __init__(self, stringRep):
        self.solved = False
        self.board = []
        self.valid = []
        lines = stringRep.split('\n')
        for line in lines:
            self.board.append([int(c) for c in line])
            self.valid.append([list(range(1,10)) for _ in line])
        self.__calculateValid()
        
    def __calculateValid(self):
        for y in range(9):
            for x in range(9):
                v = self.board[y][x]
                if v != 0:
                    self.__fillAndMarkInvalid(y, x, v)

    def __findFillablePlace(self):
        # find values that can be put only in one place
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    if len(self.valid[y][x]) == 1:
                        return (y, x, self.valid[y][x][0])
                    for v in self.valid[y][x]:
                        if self.__isOnlyOptionInRow(v, y):
                            return (y, x, v)
                        if self.__isOnlyOptionInColumn(v, x):
                            return (y, x, v)
                        if self.__isOnlyOptionInSquare(v, y, x):
                            return (y, x, v)

    def __isOnlyOptionInRow(self, value, y):
        count = 0
        for x in range(9):
            if value in self.valid[y][x]:
                count += 1
                if count > 1:
                    return False
        return True

    def __isOnlyOptionInColumn(self, value, x):
        count = 0
        for y in range(9):
            if value in self.valid[y][x]:
                count += 1
                if count > 1:
                    return False
        return True

    def __isOnlyOptionInSquare(self, value, y, x):
        count = 0
        squareX = x // 3 * 3
        squareY = y // 3 * 3
        for i in range(9):
            sx = squareX + i % 3
            sy = squareY + i // 3
            if value in self.valid[sy][sx]:
                count += 1
                if count > 1:
                    return False
        return True

    def __fillAndMarkInvalid(self, y, x, value):
        self.board[y][x] = value
        self.valid[y][x] = []
        # row
        for i in range(9):
            options = self.valid[y][i]
            if value in options:
                options.remove(value)
        # column
        for i in range(9):
            options = self.valid[i][x]
            if value in options:
                options.remove(value)
        # square
        squareX = x // 3 * 3
        squareY = y // 3 * 3
        for i in range(9):
            sx = squareX + i % 3
            sy = squareY + i // 3
            options = self.valid[sy][sx]
            if value in options:
                options.remove(value)

    def __fillNextPlace(self):
        coords = self.__findFillablePlace()
        if coords:
            y,x,v = coords
            # fill
            self.__fillAndMarkInvalid(y, x, v)
            return True
        return False

    def print(self):
        for y in range(9):
            line = ""
            for x in range(9):
                line += str(self.board[y][x])
                line += '¦' if x == 2 or x == 5 else ' '
            print(line.replace("0",' '))
            if y == 2 or y == 5:
                print('-----+-----+-----')
    
    def solveBruteForce(self, y, x):
        if y == 9:
            self.solved = True
            return
        elif self.board[y][x] != 0:
            if x == 8:
                self.solveBruteForce(y+1, 0)
            else:
                self.solveBruteForce(y, x+1)
        else:
            for v in self.valid[y][x]:
                if self.__isValidMove(x, y, v):
                    self.board[y][x] = v
                    if x == 8:
                        self.solveBruteForce(y+1, 0)
                    else:
                        self.solveBruteForce(y, x+1)
                    if self.solved:
                        return
                    self.board[y][x] = 0

    def __isValidMove(self, x, y, v):
        for i in range(9):
            if self.board[i][x] == v or self.board[y][i] == v:
                return False
        squareX = x // 3 * 3
        squareY = y // 3 * 3
        for i in range(9):
            sx = squareX + i % 3
            sy = squareY + i // 3
            if self.board[sy][sx] == v:
                return False
        return True
    
    def __isFilled(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    return False
        return True

    def solve(self):
        while self.__fillNextPlace():
            pass
        if self.__isFilled():
            return True
        else:
            # continue with brute force
            self.solveBruteForce(0,0)
            return self.solved


