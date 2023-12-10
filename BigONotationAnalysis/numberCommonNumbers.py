'''
1. Listen... for clues
     > "Given two arrays that are sorted and distinct, find the number of elements in common."

     - Optimal answer depends on clue that the interviewer is giving. 
     - If your answer doesn't use clue, it's probably not optimal.

          >> Here, **Sorting** is a clue.

2. Draw an example: large & generic

     - If the interviewer didn't told us that the arrays are the same length, don't come up with
  an example where 2 arrays are the same length.
     - If the interviewer didn't told us that the arrays are sorted, then don't assume they're sorted.

3. Brute force => Coming up with something, even if it's brute forced, is better than nothing.
4. Optimize => If came up with something slow, just state the runtime & do an effort to optimize.
5. Walk through the algorithm => make sure you know exactly what you're doing before you code.
6. Once you're all done, look for any improvements.
'''

# Brute force
def find_number_of_common_numbers(array1, array2):
     if (array1[-1] < array2[0]) or (array2[-1] < array1[0]):
          return 0
     count = 0
     dictionary = dict()
     if (len(array1) < len(array2)):
          for a in array1:
               dictionary[a] = 0
          for a in array2:
               if a in dictionary:
                    count += 1
     else:
          for a in array2:
               dictionary[a] = 0
          for a in array1:
               if a in dictionary:
                    count += 1
     
     return count

def binary_search(arr, elem):
     l = len(arr)
     if l == 0:
          return False
     if arr[l//2] == elem:
          return True
     elif arr[l//2] > elem:
          return binary_search(arr[:l//2], elem)
     else:
          return binary_search(arr[l//2 + 1:], elem)


# Optimized => O(n * log(n))
def find_number_of_common_numbers_optimized(array1, array2):
    common_count = 0

    for elem1 in array1:
        if binary_search(array2, elem1):
            common_count += 1

    return common_count


# print(find_number_of_common_numbers([1,2,3,4,5], [3,4,5])) # 3
# print(find_number_of_common_numbers([10,20,30,40,50], [1,2,3,4,5])) # 0
# print(find_number_of_common_numbers([2,4,6,8], [1,3,5,7,9])) # 0
# print(find_number_of_common_numbers([3,5,8], [1,3,5,7,9])) # 2

print(find_number_of_common_numbers_optimized([1,2,3,4,5], [3,4,5])) # 3
print(find_number_of_common_numbers_optimized([10,20,30,40,50], [1,2,3,4,5])) # 0
print(find_number_of_common_numbers_optimized([2,4,6,8], [1,3,5,7,9])) # 0
print(find_number_of_common_numbers_optimized([3,5,8], [1,3,5,7,9])) # 2
