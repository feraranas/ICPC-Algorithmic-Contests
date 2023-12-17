def gridTraveler(m,n):
     table = [[0] * (n + 1) for i in [0] * (m + 1)]

     table[1][1] = 1

     for i in range(len(table)):
          for j in range(len(table[0])):
               currentValue = table[i][j]
               if i + 1 <= m:
                    table[i + 1][j] += currentValue
               if j + 1 <= n:
                    table[i][j + 1] += currentValue 

     return table[m][n]

print(gridTraveler(1, 1)) # 1
print(gridTraveler(2, 3)) # 3
print(gridTraveler(3, 2)) # 3
print(gridTraveler(3, 3)) # 6
print(gridTraveler(18, 18)) # 6