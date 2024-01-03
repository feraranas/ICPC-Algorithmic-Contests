'''
1. the value at index i must be the maximum element in the contiguous subarrays
2. contiguous subarrays must either start from or end on index i


arr = [3, 4, 1, 6, 2]
       ^
       0 => [3] = 1
       
          ^
          1 => [4], [3, 4], [4, 1] = 3
          
             ^
             2 => [1] = 1
                
                ^
                3 => [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6] = 5
                
                    ^
                    4 => [2] = 1
                    
output = [1, 3, 1, 5, 1]

arr = [1, 1, 1, 1, 1]

       ^
       0  => [1] = 1
          
          ^
          1 => [1] = 1
          
             ^
             2 => [1] = 1
             
                ^
                3 => [1] = 1
                
                   ^
                   4 => [1] = 1
                   
                   
Output = [1, 1, 1, 1, 1]

Iterate over each number in the input arr # O(a)
Start a counter at 1, start a max variable to the index number
Iterate to the right, for each number, if it's bigger or equal return counter, else counter += 1 until the barriers of the arr # O(b)
Iterate to the left, if it's bigger or equal return counter, else counter += 1 until the barriers of the arr # O(c)

O(a * (b + c))

'''

import math

def count_subarrays(arr):
  # Write your code here
  result = []
  for i in range(len(arr)): # O(a)
    counter = 1
    maximum_value = arr[i]
    
    # the traversal to the left 
    for j in range(i - 1, -1, -1): # O(b)
      if arr[j] < maximum_value:
        counter += 1
      else:
        break
      
    # the traversal to the right
    for k in range(i + 1, len(arr)): # O(c)
      if arr[k] < maximum_value:
        counter += 1
      else:
        break
        
    result.append(counter)
  return result
      
      
  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  