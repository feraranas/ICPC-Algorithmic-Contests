'''
O(2^(n/2)) = O(2^n) Time Complexity
O(n/2) = O(n) Space complexity
'''
def lib(n):
     if n <= 1:
          return
     lib(n - 2)
     lib(n - 2)