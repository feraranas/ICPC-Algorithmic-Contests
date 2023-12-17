def canSum(targetSum, arr):
     if targetSum == 0:
          return True
     
     if targetSum < 0:
          return False
     
     # Branch for every number of the number's array
     for i in arr:
          remainder = targetSum - i
          if canSum(remainder, arr):
               return True
     return False

print(canSum(7, [5,3,4,7])) # true
print(canSum(7, [2,4])) # false
print(canSum(7, [2,3])) # true
# print(canSum(300, [7,14])) # false

print()
print()
print()

# focus on what LOC truly impacts the return value
def canSumMemoized(targetSum, arr, memo = {}):
     if (targetSum, tuple(arr)) in memo:
          return memo[(targetSum, tuple(arr))]
     if targetSum == 0:
          return True
     if targetSum < 0:
          return False
     for i in arr:
          remainder = targetSum - i
          if canSumMemoized(remainder, arr, memo):
               memo[targetSum, tuple(arr)] = True
               return True
     memo[targetSum, tuple(arr)] = False
     return False



print(canSumMemoized(7, [5,3,4,7])) # true
print(canSumMemoized(7, [2,4])) # false
print(canSumMemoized(7, [2,3])) # true
print(canSumMemoized(8, [2,3,5])) # true
print(canSumMemoized(300, [7,14])) # false
