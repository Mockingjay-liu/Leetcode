class Solution:
    def numIslands(self, grid):
        answer = 0
        flag = [[0] * (len(grid[0])) for i in range(len(grid))]
        def update(x, y):
            if x - 1 >= 0:
                if grid[x - 1][y] == '1' and flag[x - 1][y] == 0:
                    flag[x - 1][y] = 1
                    update(x - 1, y)
                else:
                    flag[x - 1][y] = 1
            if x + 1 < len(flag):
                if grid[x + 1][y] == '1' and flag[x + 1][y] == 0:
                    flag[x + 1][y] = 1
                    update(x + 1, y)
                else:
                    flag[x + 1][y] = 1
            if y - 1 >= 0:
                if grid[x][y - 1] == '1' and flag[x][y - 1] == 0:
                    flag[x][y - 1] = 1
                    update(x, y - 1)
                else:
                    flag[x][y - 1] = 1
            if y + 1 < len(flag[0]):
                if grid[x][y + 1] == '1' and flag[x][y + 1] == 0:
                    flag[x][y + 1] = 1
                    update(x, y + 1)
                else:
                    flag[x][y + 1] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if flag[i][j] == 0 and grid[i][j] == '1':
                    answer += 1
                    flag[i][j] = 1
                    update(i, j)
        return answer

S = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(S.numIslands(grid))