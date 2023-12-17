# Fibonacci

<h2>Description</h2>

Write a function fib(n) that takes in a number as an argument. 

The function should return the n-th number of the fibonacci sequence.

The 1st and 2nd number of the sequence is 1.

To generate the next number of the sequence, we sum the previous two.

<h2>Example</h2>

Input: n = [1,2,3,4,5,6,7,8,9]

Output: fib(n) = [1,1,2,3,5,8,13,21,24]

<h2>Optimize via memoization</h2>

<h2>Complexity</h2>

<h3>w/o memoization</h3>
- $O(2^n)$ time complexity w/o memoization
- $O(n)$ space complexity w/o memoization

<h3>w memoization</h3>
- $O(n)$ time complexity w memoization
- $O(n)$ space complexity w memoization

<h2>Memoization</h1>

It's an argument to our function, ideally it's a hash map / dictionary.

