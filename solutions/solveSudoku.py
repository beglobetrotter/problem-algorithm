class Solution:
    # Solution 1
    # def solveSudoku(self, board):
    #     self.board = board
    #     self.solveSudokuDFS(0, 0)
    #
    # def solveSudokuDFS(self, r, c):
    #     if r == 9:
    #         return True
    #     if c == 9:
    #         return self.solveSudokuDFS(r + 1, 0)
    #     if self.board[r][c] != '.':
    #         return self.solveSudokuDFS(r, c + 1)
    #     for value in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    #         if self.isSudoValid(r, c, value):
    #             self.board[r][c] = value
    #             if self.solveSudokuDFS(r, c + 1):
    #                 return True
    #             self.board[r][c] = '.'
    #     return False
    #
    # def isSudoValid(self, row, col, value):
    #     boxrow = row - row % 3
    #     boxcol = col - col % 3
    #     for c in range(9):
    #         if self.board[row][c] == value:
    #             return False
    #     for r in range(9):
    #         if self.board[r][col] == value:
    #             return False
    #     for r in range(boxrow, boxrow + 3):
    #         for c in range(boxcol, boxcol + 3):
    #             if self.board[r][c] == value:
    #                 return False
    #     return True

    # Solution 2
    def solveSudoku(self, board):
        self.board = board
        self.val = self.possibleVals()
        self.solveSudokuDFS()

    def possibleVals(self):
        allValues = "123456789"
        exist, val = {}, {}
        for r in range(9):
            for c in range(9):
                cell = self.board[r][c]
                if cell != '.':
                    exist[("r", r)] = exist.get(("r", r), []) + [cell]
                    exist[("c", c)] = exist.get(("c", c), []) + [cell]
                    exist[(r // 3, c // 3)] = exist.get((r // 3, c // 3), []) + [cell]
                else:
                    val[(r, c)] = []
        for (r, c) in val.keys():
            exclude = exist.get(("r", r), []) + exist.get(("c", c), []) + exist.get((r // 3, c // 3), [])
            val[(r, c)] = [num for num in allValues if num not in exclude]
        return val

    def solveSudokuDFS(self):
        if len(self.val) == 0:
            return True
        chosenKey = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[chosenKey]
        for n in nums:
            update = {chosenKey : self.val[chosenKey]}
            if self.isSudoValid(n, chosenKey, update):  # valid choice
                if self.solveSudokuDFS():  # keep solving
                    return True
            self.undo(chosenKey, update)  # invalid choice or didn't solve it => undo
        return False

    def isSudoValid(self, n, chosenKey, update):
        r, c = chosenKey
        self.board[r][c] = n
        del self.val[chosenKey]
        for key in self.val.keys():
            if n in self.val[key]:
                if key[0] == r or key[1] == c or (key[0] // 3, key[1] // 3) == (r // 3, c // 3):
                    self.val[key].remove(n)
                    update[key] = n
                    if len(self.val[key]) == 0:
                        return False
        return True

    def undo(self, chosenKey, update):
        self.board[chosenKey[0]][chosenKey[1]] = '.'
        for key in update:
            if key not in self.val:
                self.val[key] = update[key]
            else:
                self.val[key].append(update[key])

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
example = Solution()
example.solveSudoku(board)
for i in range(9):
    print(board[i])