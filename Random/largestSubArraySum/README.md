# Largest Subarray Sum

- There's an array of integers, I need to find the largest sum across all contiguous subarrays.

Things to consider:

1. Can numbers be negative? -> Yes
2. Could the answer be an empty subarray? -> No, the subarray must contain at least one element.

Let's analyze the problem

- What do we know about all subarrays? (Including the one with largest contiguous sum which we're looking for) it ends in any of the [0, 1, ... , n - 1] indices of the array.

- Is it useful if we store the largest contiguous sum for all arrays ending in each index?

Can we do better?

- Note that in our previous solution we're repeating a lot of computations, summing the same entries of the array over and over again. Can we save some of this information to achieve a faster solution?


E.g. if we have the array [-2,3,4,-5,10,-7]
the above data would be   [-2,3,7,2,12,5]

(1) Do we have the answer to the problem?
- Just take the max from the values we've computed!

(2) Do we need to store all largest subarrays sums ending in each index?
- To compute each value we just needed to know the largest subarray sum from the previous index.
