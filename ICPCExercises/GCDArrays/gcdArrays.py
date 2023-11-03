'''
Consider the array 𝑎 composed of all the integers in the range [𝑙,𝑟]. For example, 
if 𝑙=3 and 𝑟=7, then 𝑎=[3,4,5,6,7].

Given 𝑙, 𝑟, and 𝑘, is it possible for gcd(𝑎) to be greater than 1 after doing the following operation at most 𝑘 times?

1. Choose 2 numbers from 𝑎.
2. Permanently remove one occurrence of each of them from the array.
3. Insert their product back into 𝑎.

gcd(𝑏) denotes the greatest common divisor (GCD) of the integers in 𝑏.

The first line of the input contains a single integer 𝑡 (1≤𝑡≤105) — the number of test cases.

The description of test cases follows.

The input for each test case consists of a single line containing 3 non-negative integers 𝑙, 𝑟, and 𝑘 (1≤𝑙≤𝑟≤109,0≤𝑘≤𝑟−𝑙).

1 1 0 => NO
3 5 1 => NO
13 13 0 => YES
4 4 0 => YES
3 7 4 => YES
4 10 3 => YES
2 4 0 => NO
1 7 3 => NO
1 5 3 => YES
'''
import random
import math
import time

random.seed(a=None, version=2)

def operations(lst, k):
    if len(lst) > 1:
        for _ in range(k):
            if len(lst) >= 2:
                a = random.randrange(0, len(lst), 1)
                b = random.randrange(0, len(lst), 1)
                while a == b:
                    a = random.randrange(0, len(lst), 1)
                    b = random.randrange(0, len(lst), 1)
                value_a = lst[a]
                value_b = lst[b]
                c = value_a * value_b
                lst.pop(a)
                lst.pop(b - 1 if b > a else b)
                lst.append(c)
            else:
                break
    if math.gcd(*lst) > 1:
        return True
    else:
        return False

def gcdArrays(l, r, k):
    a = []
    if l <= r and k > -1:
        for i in range(l, r + 1):
            a.append(i)
    else:
        raise ValueError("Invalid input parameters")
    result = operations(a, k)
    if result:
        print("YES")
    else:
        print("NO")

t = int(input())
arr = []
for _ in range(t):
    p = input().split(' ')
    p = list(map(int, p))
    arr.append(p)

# start_time = time.time()
for i in range(len(arr)):
    gcdArrays(arr[i][0], arr[i][1], arr[i][2])
# end_time = time.time()

# print("Execution Time:", end_time - start_time, "seconds")
     

# gcdArrays(1, 1, 0)
# gcdArrays(3, 5, 1)
# gcdArrays(13, 13, 0) 
# gcdArrays(4, 4, 0) 
# gcdArrays(3, 7, 4) 
# gcdArrays(4, 10, 3) 
# gcdArrays(2, 4, 0)
# gcdArrays(1, 7, 3)
# gcdArrays(1, 5, 3) 