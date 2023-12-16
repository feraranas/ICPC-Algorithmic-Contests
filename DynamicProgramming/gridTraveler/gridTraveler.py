# w/o memoization
def gridTraveler(m,n):
     if m == 1 and n == 1:
          return 1
     if m == 0 or n == 0:
          return 0
     return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

print(gridTraveler(1, 1)) # 1
print(gridTraveler(2, 3)) # 3
print(gridTraveler(3, 2)) # 3
print(gridTraveler(3, 3)) # 6

# w memoization
def gridTravelerMemoV1(m,n,memo = {}):
     if memo.get((m,n)):
          return memo[(m,n)]
     if m == 1 and n == 1:
          return 1
     if m == 0 or n == 0:
          return 0
     memo[(m,n)] = gridTravelerMemoV1(m - 1, n, memo) + gridTravelerMemoV1(m, n - 1, memo)
     return memo[(m,n)]

print(gridTravelerMemoV1(18, 18)) # 2333606220

def gridTravelerMemoV2(m,n,memo = {}):
     key = m, ',', n
     if memo.get(key):
          return memo[key]
     if m == 1 and n == 1:
          return 1
     if m == 0 or n == 0:
          return 0
     memo[key] = gridTravelerMemoV2(m - 1, n, memo) + gridTravelerMemoV2(m, n - 1, memo)
     return memo[key]

print(gridTravelerMemoV2(18, 18)) # 2333606220

'''
In terms of functionality, there is no difference between the two functions `gridTravelerMemoV1` and `gridTravelerMemoV2`. 
Both functions use memoization to store and retrieve previously computed results for specific inputs, and they produce the same results for the same inputs.

The only difference lies in how the keys are constructed for the `memo` dictionary:

1. In `gridTravelerMemoV1`, the keys are tuples `(m, n)`.
2. In `gridTravelerMemoV2`, the keys are strings `"m,n"`.

The choice between these two approaches is mostly a matter of personal preference or specific requirements. 
Tuples are a natural choice for representing pairs of values, and they are often used as keys in dictionaries. 
On the other hand, using a string as a key with a specific format (e.g., `"m,n"`) is also a valid approach, especially if you prefer a string representation.

From a performance perspective, the impact of the choice is likely minimal. Tuples and strings are both hashable types, 
which is important for dictionary keys, and the overall efficiency will depend on other factors in your specific use case.
It's more common to see tuples used in such scenarios, but both approaches are technically correct.
'''