'''
First line is O(a).
Second nested loop is O(a^2)

If O(a^2 + a^2) is equivalent to O(a^2), then
certainly O(a + a^2) is equivalent to O(a^2)

Then, generalizing:
- O(a^2 + a) ==> O(a^2)
- O(d + a^2) ==> O(d + a^2)
- O(a^5 + a^2) ==> O(a^5)
- O(2^n + a^2) ==> O(2^n)
'''

def count_pairs_which_sum_to_max(array):
     max_value = max(array) # O(a)
     count = 0 
     for left in range(0, len(array)):
          for right in range(left + 1, len(array)):
               left_value = array[left]
               right_value = array[right]
               if left_value + right_value == max_value:
                    count += 1
     return count