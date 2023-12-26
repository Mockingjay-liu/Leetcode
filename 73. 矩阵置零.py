import numpy as np
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        x = np.array(matrix)
        zeros = np.argwhere(x == 0)
        for i in zeros:
            matrix[i[0]] = [0]*n
            for j in range(m):
                matrix[j][i[1]] = 0
        return matrix

S = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(S.setZeroes(matrix))