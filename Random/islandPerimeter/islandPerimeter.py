from typing import List

class Solution:
    def __init__(self, p=0):
        self.p = p
        self.tlrd = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        def islandPerimeterUtil(i, j):
            tmp = 0
            if grid[i][j] == 1:
                tmp = 4
                for k in self.tlrd:
                    n = i + k[0]
                    m = j + k[1]
                    if (n >= 0 and m >= 0) and (n < r and m < c):
                        if grid[n][m] == 1 or grid[n][m] == -1:
                            tmp -= 1
                grid[i][j] = -1
            return tmp


        for i in range(r):
            for j in range(c):
                self.p += islandPerimeterUtil(i, j)
        
        return self.p
    
with open('matrix.txt', 'r') as file:
    matrix = [list(map(int, line.split())) for line in file]

solution = Solution()
print(solution.islandPerimeter(matrix))