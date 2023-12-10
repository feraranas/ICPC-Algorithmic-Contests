'''
Big O Analysis

1. The outer loop has a time complexity of O(n), where n is the length of the input array. 
   This is because the loop runs once for each element in the array.

2. The inner loop runs for each even element a and has a time complexity of O(a), 
   where a is the value of the even element. This is because it prints numbers from 0 to a.

Now, let's consider the **worst-case scenario**. If all elements in the array are even and have different values, 
the inner loop would run different numbers of times for each element. In this case, the overall time complexity
would be the sum of the time complexities of each iteration.

So, the worst-case time complexity of the entire function is:
O(n) + O(a1) + O(a2) + ... + O(an)
O(n + a1 + a2 + ... + an), where a1, a2, ..., an are the even elements in the array.

In Big O notation, we usually focus on the **dominant term**, and in this case, the dominant term is the largest 
even element in the array. Therefore, we can simplify the expression to O(max(a1, a2, ..., an)).

Say max(a1, a2, ..., an) = k

Then:
O(a*k) time complexity 
- Where a: size of the array
-       k: largest even number
'''
def print_even_sequence(array):
  for a in array:
    if a % 2 == 0:
      print("sequence for {0}".format(a))
      for k in range(0,a):
        print(k, end=" ")
  print()  

print_even_sequence([1,2,3,5])