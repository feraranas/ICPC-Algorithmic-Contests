'''
Madoka finally found the administrator password for her computer. 
Her father is a well-known popularizer of mathematics, so the password is the answer to the following problem.

Find the maximum decimal number without zeroes and with no equal digits in a row, such that the sum of its digits is 𝑛.

Madoka is too tired of math to solve it herself, so help her to solve this problem!

Each test contains multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤1000) — the number of test cases.

Description of the test cases follows.

The only line of each test case contains an integer 𝑛 (1≤𝑛≤1000) — the required sum of the digits.

For each test case print the maximum number you can obtain.

Input | Output
5       # test cases
1       1
2       2
3       21
4       121
5       212

Note: 
The only numbers with the sum of digits equal to 2 without zeros are 2 and 11. 
But the last one has two ones in a row, so it's not valid. That's why the answer is 2.

The only numbers with the sum of digits equal to 3 without zeros are 111, 12, 21, and 3. The first one has 2
ones in a row, so it's not valid. So the maximum valid number is 21.

The only numbers with the sum of digits equals to 4 without zeros are 1111, 211, 121, 112, 13, 31, 22, and 4. 
Numbers 1111, 211, 112, 22 aren't valid, because they have some identical digits in a row.
So the maximum valid number is 121.
'''

