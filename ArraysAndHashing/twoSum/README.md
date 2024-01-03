# Two Sum

Description:

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

<h3>Example 1:</h3>

> Input: nums = [2,7,11,15], target = 9

> Output: [0,1]

> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

<h3>Example 2:</h3>

> Input: nums = [3,2,4], target = 6

> Output: [1,2]

<h3>Example 3:</h3>

> Input: nums = [3,3], target = 6

> Output: [0,1]
 

<h3>Constraints:</h3>

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

<h3>Pseudocode</h3>

- Initialize an empty dictionary (d)
- Iterate through the array
- For each number in array, calculate its complement (target - number)
- If complement (value) in dictionary, return the key and the index of current number
- Else add key->(current index) and value->(currentnumber) to the dictionary (d)

<h3>Complexity</h3>

The time complexity of the twoSum function is O(n), where n is the number of elements in the nums list. Let's break down the reasoning:

The function iterates through each element in the nums list exactly once using a for loop. This contributes O(n) to the time complexity.

Inside the loop, the function calls the find_key function, which iterates through the items of the dictionary (d) to find a key with a specific value. In the worst case, this operation can be O(n), where n is the number of elements in the dictionary. However, since the dictionary is built incrementally and only contains elements encountered so far, on average, the number of elements in the dictionary will be much smaller than n. Therefore, the overall time complexity of the find_key function can be considered closer to O(1) on average.

Considering the loop dominates the time complexity, and the find_key function is closer to O(1) on average, the overall time complexity of the twoSum function is O(n).