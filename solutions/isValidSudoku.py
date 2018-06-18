class Solution:
    def isValidSudoku(self, board):
        sudokuTuple = []
        for i, row in enumerate(board):
            for j, cellValue in enumerate(row):
                if cellValue != '.':
                    sudokuTuple.append((cellValue, i))
                    sudokuTuple.append((j, cellValue))
                    sudokuTuple.append((i // 3, j // 3, cellValue))
        return len(sudokuTuple) == len(set(sudokuTuple))

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
print(example.isValidSudoku(board))