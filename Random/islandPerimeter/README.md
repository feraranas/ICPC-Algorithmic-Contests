# Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

<h3>Example 1:</h3>

<img width=300px src="island.png">

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image above.

<h3>Example 2:</h3>

Input: grid = [[1]]

Output: 4

<h3>Example 3:</h3>

Input: grid = [[1,0]]

Output: 4
 

<h3>Constraints</h3>

- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 100
- grid[i][j] is 0 or 1.
- There is exactly one island in grid.

References

(leetcode)[https://leetcode.com/problems/island-perimeter/]