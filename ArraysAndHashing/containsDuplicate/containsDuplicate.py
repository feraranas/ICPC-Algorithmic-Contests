from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for i in nums: # O(n)
            if i in dictionary: 
                return True
            dictionary[i] = 0

        return False
    
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        dictionary = set()

        for i in nums: # O(n)
            if i in dictionary: 
                return True
            dictionary.add(i)

        return False
    
    def containsDuplicateSet2(self, nums: List[int]) -> bool:
        nums1 = set(nums) # store each unique element
        return not len(nums1) == len(nums)
    
    def containsDuplicateSort(self, nums: List[int]) -> bool:
        nums.sort() # sorts in place
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
    
    def containsDuplicateCounter(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        for x in nums.values():
            if x > 1:
                return True
        return False