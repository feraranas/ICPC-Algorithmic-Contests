# w/o memoization
def howSum(targetSum, arr):
     if targetSum == 0:
          return []
     
     if targetSum < 0:
          return None
     
     for num in arr:
          
          remainder = targetSum - num

          remainderResult = howSum(remainder, arr)

          if remainderResult != None:
               return [*remainderResult, num]
     
     return None

print(howSum(7, [2,3])) # [3, 2, 2]
print(howSum(3, [1,2])) # [2, 1]
print(howSum(7, [2,4])) # None
print(howSum(8, [2,3,5])) # [2, 2, 2, 2]

print()
print()
print()

def howSumMemoized(targetSum, arr, memo = {}):
     if targetSum in memo:
          return memo[targetSum]
      
     if targetSum == 0:
          return []
     
     if targetSum < 0:
          return None
     
     for num in arr:
          
          remainder = targetSum - num

          remainderResult = howSumMemoized(remainder, arr, memo)

          if remainderResult != None:
               memo[targetSum] = [*remainderResult, num]
               return memo[targetSum]
     
     memo[targetSum] = None
     return None

print(howSumMemoized(7, [2,3])) # [3, 2, 2]
print(howSumMemoized(3, [1,2])) # [2, 1]
print(howSumMemoized(7, [2,4])) # None
print(howSumMemoized(8, [2,3,5])) # [2, 2, 2, 2]
print(howSumMemoized(300, [7, 14])) # None