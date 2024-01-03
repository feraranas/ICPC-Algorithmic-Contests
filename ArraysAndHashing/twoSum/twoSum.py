from typing import List

# Brute force
# class Solution:
#     def twoSum(nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     print([i, j])

# Optimized

def find_key(input_dict, value):
   return next((k for k, v in input_dict.items() if v == value), None)

# Optimum Speed
def twoSum(nums: List[int], target: int) -> List[int]:
     d = dict()
     for idx, i in enumerate(nums):
          c = target - i
          k = find_key(d, c)
          if k != None:
               return [k, idx]
          else:
               d[idx] = i
     return []

# Optimum Memory
def twoSumOptimumMemory(nums: List[int], target: int) -> List[int]:
   pred = {} # predicate -> i
   for i, n in enumerate(nums):
       p = target - n
       if p in pred:
           return [pred[p], i]
       pred[n] = i

   return []

print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSumOptimumMemory([2,7,11,15], 9)) # [0,1]
print(twoSumOptimumMemory([3,2,4], 6)) # [1,2]