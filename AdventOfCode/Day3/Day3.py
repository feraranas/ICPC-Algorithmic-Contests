'''
Pseudocode:
(1) Iterate over each row and over each column.

(2) If a period or a symbol is found just continue to the next column.

(3) If a number is found: save the column index in a queue, save  a temporary 
    string  with  the   number,   then continue to next column to the   right.  
    If  this  column  is   again  a  number,  do  the same: add  column index 
    to queue, append number to the end of temporary string, then  continue to 
    the next column. Stop  when  a  new  period  is  found.

(4) We'll call each number in the queue so that it checks the 9 surrounding positions.
     If any number in any surrounding position contains a symbol [*, %, #, $, +, ...]
     we abandon the queue search, then convert the temporary string to an integer and
     add it to the overall sum.
'''

def partOne(matrix):
     
     sum = 0

     ascii_symbols = [chr(i) for i in range(33, 127)]

     if '.' in ascii_symbols:
         ascii_symbols.remove('.')

     def checkSurroundings(i, j):
          for i in range(-1, 2):
               for j in range(-1, 2):
                    a = 1

     r = len(matrix)
     c = len(matrix[0])
     for i in range(r):
          tmp = ''
          for j in range(c):
               if matrix[i][j].isnumeric():
                    
          

if __name__ == '__main__':
     
     matrix = []
     with open('puzzle.txt', 'r') as file:
          for line in file:
               row = [c for c in line]
               matrix.append(row)

     sum = partOne(matrix)
     