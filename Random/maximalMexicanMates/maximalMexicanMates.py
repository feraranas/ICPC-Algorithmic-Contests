def largest_maximal_mexican_region(matrix):
     r = len(matrix)
     c = len(matrix[0])

     def _maximal_mexican_region(i, j):
          # base case: we're done filling from this cell
          if i >= r or j >= c or matrix[i][j] == 0:
               return 0
          
          # mark the cell as visited
          matrix[i][j] = 0
          
          s = 1
          
          # visit all directions
          for k in range(-1, 2):
               for l in range(-1, 2):
                    s += _maximal_mexican_region(i + k, j + l)
          
          return s
     
     maximal = 0
     for i in range(r):
          for j in range(c):
               maximal = max(maximal, _maximal_mexican_region(i, j))

     return maximal


matrix_file_path = 'inputMatrix1.txt'

# Read the matrix from the file
with open(matrix_file_path, 'r') as file:
    matrix = [list(map(int, line.split())) for line in file]

print(largest_maximal_mexican_region(matrix))