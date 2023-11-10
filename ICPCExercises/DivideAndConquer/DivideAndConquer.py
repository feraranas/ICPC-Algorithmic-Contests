'''
///====================================================================================///
An array 𝑏 is good if the sum of elements of 𝑏 is even.

You are given an array 𝑎 consisting of 𝑛 positive integers. In one operation, you can select an index and change 𝑎𝑖:=⌊𝑎𝑖 / 2⌋†

 Find the minimum number of operations (possibly 0) needed to make 𝑎 good.
 It can be proven that it is always possible to make 𝑎
 good.

⌊𝑥⌋† denotes the floor function — the largest integer less than or equal to 𝑥. For example, ⌊2.7⌋=2, ⌊𝜋⌋=3 and ⌊5⌋=5.


///====================================================================================///

Each test contains multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤100) — the number of test cases.
The description of the test cases follows.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤50) — the length of the array 𝑎.

The second line of each test case contains 𝑛 space-separated integers 𝑎1,𝑎2,…,𝑎𝑛(1≤𝑎𝑖≤106) — representing the array 𝑎.

Do note that the sum of 𝑛 over all test cases is not bounded.

'''

import math

# def divide_and_conquer(l, n):
#     if sum(l) % 2 == 0:
#         return 0
#     if len(l) == 1:
#         return 1 + divide_and_conquer([math.floor(l[0] / 2)], len([math.floor(l[0] / 2)]))
#     return divide_and_conquer(l[:math.floor(len(l) / 2)], len(l)) + divide_and_conquer(l[math.floor(len(l) / 2):], len(l))


def main():
    n = int(input())
    for i in range(n):
        listLen = int(input())
        listValues = input()
        list = [int(i) for i in listValues.split(' ')]
        print(dc(list, listLen))
    

if __name__ == "__main__":
    main()


# 4
# 4
# 1 1 1 1   Output: 0
# 2
# 7 4       Output: 2
# 3
# 1 2 4     Output: 1
# 1
# 15        Output: 4