from collections import deque
from typing import List

class Solution:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def printMatrix(self, matrix: List[List[int]]):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")

            print()

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        memo = {}
        
        r,c = len(image), len(image[0])
        
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        queue = deque([(sr, sc)])

        st = image[sr][sc]

        while queue:
            sr, sc = queue.popleft()
            
            image[sr][sc] = color

            for d in directions:
                nsr = sr + d[0]
                nsc = sc + d[1]
                if nsr >= 0 and nsr < r and nsc >=0 and nsc < c:
                    if image[nsr][nsc] == st and not memo.get((nsr, nsc)):
                        memo[(nsr, nsc)] = 1
                        queue.append((nsr, nsc))

        self.printMatrix(image)
        return image
    
with open('matrix.txt', 'r') as file:
    matrix = [list(map(int, line.split())) for line in file]
    solution = Solution(matrix)
    nmatrix = solution.floodFill(matrix, 1, 1, 2)
