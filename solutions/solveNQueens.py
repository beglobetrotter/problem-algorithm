class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                print(p, q)
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
    #     self.board = [['.'] * n] * n
    #     self.solveQueensDFS(0, 0, n)
    #
    # def solveQueensDFS(self, r, c, n):
    #     if r == n: return True
    #     if c == n: return self.solveQueensDFS(r + 1, 0, n)
    #
    #     chosenKey = min(self.val.keys(), key=lambda x: len(self.val[x]))
    #     nums = self.val[chosenKey]
    #     for n in nums:
    #         update = {chosenKey: self.val[chosenKey]}
    #         if self.isSudoValid(n, chosenKey, update):  # valid choice
    #             if self.solveQueensDFS():  # keep solving
    #                 return True
    #     return False
    #
    # def isSudoValid(self, n, chosenKey, update):
    #     r, c = chosenKey
    #     self.board[r][c] = n
    #     del self.val[chosenKey]
    #     for key in self.val.keys():
    #         if n in self.val[key]:
    #             if key[0] == r or key[1] == c or (key[0] // 3, key[1] // 3) == (r // 3, c // 3):
    #                 self.val[key].remove(n)
    #                 update[key] = n
    #                 if len(self.val[key]) == 0:
    #                     return False
    #     return True

example = Solution()
print(example.solveNQueens(4))
