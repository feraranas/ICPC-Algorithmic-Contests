'''
O(2^n) time complexity
O(n) space complexity
'''
def dib(n):
     if n <= 1:
          return
     dib(n - 1)
     dib(n - 1)