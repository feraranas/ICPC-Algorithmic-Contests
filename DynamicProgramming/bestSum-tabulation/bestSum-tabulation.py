def bestSumTabulation(targetSum, numbers):
     table = [None] * (targetSum + 1)

     table[0] = []

     for i in range(len(table)):
          if table[i] != None:
               for num in numbers:
                    if i + num < len(table):
                         # prefer / keep the shorter array
                         candidateCombination = [*table[i], num]
                         if table[i + num] == None or len(table[i + num]) > len(candidateCombination):
                              table[i + num] = candidateCombination
     
     return table[targetSum]

print(bestSumTabulation(7, [5,3,4,7])) # [7]
print(bestSumTabulation(8, [2,3,5])) # [3,5]
print(bestSumTabulation(8, [1,4,5])) # [4,4]
print(bestSumTabulation(100, [1,2,5,25])) # [25,25,25,25]