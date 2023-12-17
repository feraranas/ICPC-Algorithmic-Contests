'''
     O(dib) <= O(fib) <= O(lib)
'''

def fibonacci(n):
     if n == 0:
          return 0
     elif n <= 2:
          return 1
     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(3)) # 2
# print(fibonacci(4)) # 3
# print(fibonacci(5)) # 5
# print(fibonacci(6)) # 8
# print(fibonacci(7)) # 13
# print(fibonacci(8)) # 21
# print(fibonacci(9)) # 34
# print(fibonacci(50)) # 12586269025

# Using memoization v1
def fibonacci_memo_v1(n, memo = {}):
     if memo.get(n):
          return memo[n]
     if n == 0:
          return 0
     elif n <= 2:
          return 1
     memo[n - 1] = fibonacci_memo_v1(n - 1)
     memo[n - 2] = fibonacci_memo_v1(n - 2)
     return memo[n - 1] + memo[n - 2]

# Using memoization v2
def fibonacci_memo_v2(n, memo = {}):
     if memo.get(n):
          return memo[n]
     if n == 0:
          return 0
     elif n <= 2:
          return 1
     memo[n] = fibonacci_memo_v2(n - 1) + fibonacci_memo_v2(n - 2)
     return memo[n]

# print(fibonacci_memo_v1(50)) # 12586269025
# print(fibonacci_memo_v2(50)) # 12586269025