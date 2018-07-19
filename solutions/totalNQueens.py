class Solution:
    def totalNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result[0] += 1
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = [0]
        DFS([], [], [])
        return result[0]

example = Solution()
print(example.totalNQueens(4))