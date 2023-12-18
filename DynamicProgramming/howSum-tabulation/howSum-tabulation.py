def howSumTabulation(target, numbers):
     table = [None] * (target + 1)
     
     table[0] = []
     
     for i in range(len(table)):
          if table[i] != None:
               for num in numbers:
                    if i + num < len(table):
                         table[i + num] = [*table[i], num]
     
     return table[target]

print(howSumTabulation(7, [2,3])) # [3, 2, 2]
print(howSumTabulation(3, [1,2])) # [2, 1]
print(howSumTabulation(7, [2,4])) # None
print(howSumTabulation(8, [2,3,5])) # [2, 2, 2, 2]

          