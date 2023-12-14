from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        dictRowsOnes = {}
        dictRowsZeros = {}
        dictColsOnes = {}
        dictColsZeros = {}
        r = len(grid)
        c = len(grid[0])

        # Initialize dictionaries with zeros
        for i in range(r):
            dictRowsOnes[i] = 0
            dictRowsZeros[i] = 0
        for j in range(c):
            dictColsOnes[j] = 0
            dictColsZeros[j] = 0
        
        nl = []
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    dictRowsOnes[i] += 1
                    dictColsOnes[j] += 1
                else:
                    dictRowsZeros[i] += 1
                    dictColsZeros[j] += 1
        
        for i in range(r):
            tl = []
            for j in range(c):
                tl.append(dictRowsOnes[i] + dictColsOnes[j] - dictRowsZeros[i] - dictColsZeros[j])
            nl.append(tl)

        return nl
    
