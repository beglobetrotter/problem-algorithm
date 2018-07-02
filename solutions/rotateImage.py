class Solution:
    def rotate(self, matrix):
        matrix[:] = matrix[::-1]
        size = len(matrix)
        for i in range(size - 1):
            for j in range(i + 1, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

example = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
example.rotate(matrix)
print(matrix)


