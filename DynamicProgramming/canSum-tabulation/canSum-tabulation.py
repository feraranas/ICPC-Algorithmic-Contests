def canSum(targetSum, numbers):
     
     table = [False] * (targetSum + 1)
     
     table[0] = True

     for i in range(len(table)):
          if table[i] == True:
               for num in numbers:
                    if i + num < len(table):
                         table[i + num] = True

     return table[targetSum]

print(canSum(7, [5,3,4,7])) # true
print(canSum(7, [2,4])) # false
print(canSum(8, [2,3,5])) # true
print(canSum(300, [7,14])) # false