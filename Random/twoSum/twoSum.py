from typing import List

# Brute force
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    print([i, j])

print(Solution.twoSum([2,7,11,15], 9)) # [0,1]
print(Solution.twoSum([3,2,4], 6)) # [1,2]