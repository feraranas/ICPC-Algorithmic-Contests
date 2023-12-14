# brute force
def find_largest_subarray_sum_brute(array):
     # we keep two pointers denoting the start and end of each subarray
     n = len(array)
     max_sum = float('-inf') 
     for i in range(n):
          # i denotes the start of the subarray, and it can end all the way from i to n-1
          for j in range(i, n):
               sub_array_sum = sum(array[i:j])
               max_sum = max(max_sum,  sub_array_sum)
     return max_sum

# optimized
def find_largest_subarray_sum_optimized(array):
     # we keep two pointers (l, r) denoting the start and end of each subarray & a 
     # variable for stamping the subarray pair of indices
     np = 0
     max_pair = (np, 0)
     n = len(array)
     largest_temporal = 0
     largest_overall =  float('-inf')
     for i in range(n):
          largest_temporal += array[i]

          if largest_temporal > largest_overall:
               largest_overall = largest_temporal
               max_pair = (np, i)
          else:
               largest_overall = largest_overall
          
          # for the next iteration the initial value of the largest_ending_here is
          # the largest sum from the previous index, we just want to append it to
          # the new index if it helps otherwise reset to zero
          if array[i] < 0:
               largest_temporal = 0
               np = i + 1

     return largest_overall, max_pair

largestSum, pair = find_largest_subarray_sum_optimized([5,4,-1,3,2,-5,1]) # 9, [0,1]
print(largestSum, pair)

largestSum, pair = find_largest_subarray_sum_optimized([5,4,3,2,-5,1]) # 14, [0,3]
print(largestSum, pair)

largestSum, pair = find_largest_subarray_sum_optimized([-1,-1,3,2,-5,1]) # 5, [2,3]
print(largestSum, pair)