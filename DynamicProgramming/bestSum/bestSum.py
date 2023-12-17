def bestSum(targetSum, arr):
     if targetSum == 0:
          return []
     
     if targetSum < 0:
          return None
     
     shortestCombination = None
     
     for num in arr:
          remainder = targetSum - num
          remainderCombination = bestSum(remainder, arr)
     
          if remainderCombination != None:
               combination = [*remainderCombination, num]

               # if combination is shorter than the current *shortest*, update it
               if shortestCombination == None or (len(combination) < len(shortestCombination)):
                    shortestCombination = combination

     return shortestCombination

print(bestSum(7, [5,3,4,7])) # [7]
print(bestSum(8, [2,3,5])) # [3,5]
print(bestSum(8, [1,4,5])) # [4,4]
# print(bestSum(100, [1,2,5,25])) # [25,25,25,25]

print()
print()
print()

def bestSumMemoized(targetSum, arr, memo = {}):
     if targetSum in memo:
          return memo[targetSum]

     if targetSum == 0:
          return []
     
     if targetSum < 0:
          return None
     
     shortestCombination = None
     
     for num in arr: # O(n)
          remainder = targetSum - num
          remainderCombination = bestSumMemoized(remainder, arr) # O(m)
     
          if remainderCombination != None:
               combination = [*remainderCombination, num] # O(n)

               # if combination is shorter than the current *shortest*, update it
               if shortestCombination == None or (len(combination) < len(shortestCombination)):
                    shortestCombination = combination

     memo[targetSum] = shortestCombination
     return shortestCombination

# print(bestSumMemoized(7, [5,3,4,7])) # [7]
# print(bestSumMemoized(8, [2,3,5])) # [3,5]
# print(bestSumMemoized(8, [1,4,5])) # [4,4]
print(bestSumMemoized(100, [1,2,5,25])) # [25,25,25,25]