# Sum String

Code: [sumString.py](sumString.py)

> Given a string of digits, determine whether it is a 'sum-string'. A string S is called a sum-string if the rightmost substring can be written as the sum of two substrings before it and the same is recursively true for substrings before.

Example 1: 
> Input "12243660" is a sum string.<br>
> Explanation: 24 + 36 = 60, 12 + 24 = 36

Example 2: 
> Input "1111112223" is a sum string.<br>
> Explanation: 111 + 112 = 223, 1 + 111 = 112

Example 3:
> Input "2368" is not a sum string.

### In general
A string S is called a sum-string if it satisfies the following properties:

```python
sub-string(i, x) + sub-string(x + 1, j) = sub-string(j + 1, 1)
and
sub-string(x + 1, j) + sub-string(j + 1, l) = sub-string(l + 1, m)
and so on till the end.
```

<details>
<summary>How does it work?</summary>

From the examples above, we can see that our decision depends on the first two chosen numbers. So we choose all possible first two numbers for a given string. Then for every chosen two numbers, we check whether it is sum-string or not?

So the approach is very simple. We generate all possible first two numbers using two substrings s1 and s2 using two loops. Then we check whether it is possible to make the number s3 = (s1 + s2) or not. If we can make s3 then we recursively check for s2 + s3 and so on.

</details>

<details>
<summary>PSEUDOCODE</summary>

```python
function checkSubstring(str):
    A function receives a string as a parameter 'str'.
    It calculates the length of the string and stores it in the variable 'n'.
    It iterates from 1 to n, using the variable 'i'.
        It iterates from 1 to n-i, using the variable 'j'.
            If checksum(str, beg, i, j) is satisfied, where beg is the start (0),
                It returns true.
    It returns false.
```

```python
function checksum(str):
function processSubstring(inputStr, startIndex, length1, length2):
    s1 = substring of inputStr from startIndex to (startIndex + length1)
    s2 = substring of inputStr from (startIndex + length1) to (startIndex + length1 + length2)
    s3 = sum s1 and s2
    s3_len = length of s3

    if s3_len > (length of inputStr - length1 - length2):
        return false

    if s3 equals substring of inputStr from (startIndex + length1 + length2) to (startIndex + length1 + length2 + s3_len):
        if end of string is reached:
            return true
        else:
            return processSubstring(inputStr, (startIndex + length1), length2, s3_len)

    return false
```

</details>

<details>
<summary>Complexity</summary>

Time Complexity: $O(n^3)$, where n is the length of the string.

Auxiliary Space: $O(n)$, where n is the length of the string.

</details>

<details>
<summary>References</summary>

1. [geekforgeeks](https://www.geeksforgeeks.org/check-given-string-sum-string/?ref=lbp)

</details>