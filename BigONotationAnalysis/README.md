<summary>BIG O, INTERVIEWING & OPTIMIZING</summary>

<hr style="border:6px dashed blue">

<details>
<summary>The general principles of Big O</summary>
<hr style="border:2px solid red">

1. Include all things: focus on sub-functions too.
2. Use logical variable names. Don't toss around n.
3. Define the variables you need.
4. Be thoughtful of when to Adding vs Multiplying.
5. Drop constants.
6. Use big O for space. Remember the call stack!
7. Drop non-dominant terms.
8. A lower big O doesn't mean always faster. It means faster when the data is sufficiently large.
9. It's about scale!
</details>

<details>
<summary>Tips on interviewing</summary>
<hr style="border:2px solid green">

1. Listen... for clues
     > "Given two arrays that are sorted and distinct, find the number of elements in common."

     - Optimal answer depends on clue that the interviewer is giving. 
     - If your answer doesn't use clue, it's probably not optimal.

          >> Here, **Sorting** is a clue.

2. Draw an example: large & generic

     - If the interviewer didn't told us that the arrays are the same length, don't come up with
  an example where 2 arrays are the same length.
     - If the interviewer didn't told us that the arrays are sorted, then don't assume they're sorted.

3. Brute force => Coming up with something, even if it's brute forced, is better than nothing.
4. Optimize => If came up with something slow, just state the runtime & do an effort to optimize.
5. Walk through the algorithm => make sure you know exactly what you're doing before you code.
6. Once you're all done, look for any improvements.
</details>

<details>
<summary>Tips on optimizing an algorithm</summary>
<hr style="border:2px solid orange">

> TECHNIQUE: OPTIMIZING WITH BUD
1. Bottlenecks
     Think of this example: 
     >Given two arrays that are sorted and distinct, find the number of elements in common.
2. Unnecessary work
     Think of this example:
     > a^3 + b^3 = c^3 + d^3
     - Sometimes getting rid of unnecessary work doesn't make a big difference,
     by itself. BUT, in conjunction with another change, it does.  
3. Duplicated work
4. Optimizing with ```SPACE``` and ```TIME```
- Consider upfront work to save yourself time down the road
     > pre-computation, tries, hash-tables
     For example: Sorting the data, creating a hash table, etc.
5. Best Conceivable Runtime: What is the best runtime you could possibly imagine getting?
     Think of this example:
     > Given an array, find all pairs that sum to the median value.
6. If your algorithm is already runtime-optimal, consider optimizng for space complexity.

</details>