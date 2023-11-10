'''
Marin wants you to count number of permutations that are beautiful. 
A beautiful permutation of length 𝑛 is a permutation that has the following property: gcd(1⋅𝑝1,2⋅𝑝2,…,𝑛⋅𝑝𝑛)>1,

where gcd is the greatest common divisor.

A permutation is an array consisting of 𝑛 distinct integers from 1 to 𝑛 in arbitrary order. For example, [2,3,1,5,4]
is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array)
and [1,3,4] is also not a permutation (𝑛=3 but there is 4 in the array).

Input
The first line contains one integer 𝑡 (1≤𝑡≤103) — the number of test cases.

Each test case consists of one line containing one integer 𝑛 (1≤𝑛≤103).

Output
For each test case, print one integer — number of beautiful permutations. 
Because the answer can be very big, please print the answer modulo 998244353.
'''

def main():
    n = int(input())
    for i in range(n):
        k = int(input())
        permutation

if __name__ == "__main__":
    main()