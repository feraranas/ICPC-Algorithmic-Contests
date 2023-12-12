# Backtracking

<details>
<summary>Backtracking definitions</summary>

1. Backtracking is an algorithm approach for finding all the possible solutions by exploring all possible ways.

2. Backtracking is like trying different paths, and when you hit a dead end, you backtrack to the last choice and try a different route. (Dead end means: one of the found solutions turns out to not satisfy the given criteria, so it discards the solution and makes some changes and backtracks again.)

3. Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end. When a dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted.

4. Is a general algorithm for finding all the solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds possible candidates to the solutions and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to finally become a valid solution. It is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

</details>

<details>
<summary>Why is it used?</summary>

1. Commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like Sudoku.

</details>

<details>
<summary>Terminologies</summary>

1. Candidate
2. Solution
3. Partial Solution
4. Decision Space
5. Decision Point
6. Feasible Solution
7. Dead End
8. Backtrack
9. Search Space
10. Optimal Solution

</details>

<details>
<summary>Types of Backtracking problems</summary>

1. Decision Problems: We search for a feasible solution.
2. Optimization Problems: We search for the best solution.
3. Enumeration Problems: We find a set of all possible feasible solutions to the problem.

</details>

<details>
<summary>How does it work?</summary>
<img width=500px src="backtracking.png">

- "IS" represents the Initial State where the recursion call starts to find a valid solution.
- "C" represents different Checkpoints for recursive calls.
- "TN" represents Terminal Nodes where no further recursive calls can be made, these nodes act as base case of recursion and we determine whether the current solution is valid or not at this state.

At each checkpoint, our program makes some decisions and move to other checkpoints until it reaches a terminal Node, after determining whether a solution is valid or not, the program starts to revert back to the checkpoints and try to explore other paths. For example in the image TN1...TN5 are the terminal nodes where the solution is not acceptable, while TN6 is the state where we found a valid solution. 

The back arrows in the images shows backtracking in action, where we revert the changes made by some checkpoint.
</details>

<details>
<summary>Determining Backtracking problems</summary>

<details>Generally every constraint satisfaction problem can be solved using backtracking but, Is it optimal to use backtracking every time? Turns out NO, there are a vast number of problem that can be solved using Greedy or Dynamic programming in logarithmic or polynomial time complexity which is far better than exponential complexity of Backtracking. However many problems still exists that can only be solved using Backtracking.</details>

To understand whether a problem is Backtracking based or not, consider a simple problem:

> Imagine you have 3 closed boxes, among which 2 are empty and 1 has a gold coin. Your task is to get the gold coin.

<details>
<summary>Why dynamic programming fails to solve this question?</summary>

Does opening or closing one box has any effect on the other box? Turns out NO, each and every box is independent of each other and opening/closing state of one box can not determine the transition for other boxes. Hence DP fails.

</details>

<details>
<summary>Why greedy fails to solve this question?</summary>

Greedy algorithm chooses a local maxima in order to get global maxima, but in this problem each and every box has equal probability of having a gold coin i.e. 1/3, hence there's no criteria to make a greedy choice.

</details>

<details>
<summary>Why backtracking works?</summary>

Backtracking algorithm is simply brute forcing each and every choice, hence we can one by one choose every box to find the gold coin, If a box is found empty we can close it back which acts as a Backtracking step.

</details>

<h5>Technically, for backtracking problems:</h5>
<ul>
     <li>The algorithm builds a solution by exploring all possible paths created by the choices in the problem, this solution begins with an empty set S = {}.</li>
     <li>Each choice creates a new sub-tree 's' which we add into the set.</li>
     <li>Now there exist two cases:
          <ol>
               <li>(S + s) is a valid set</li>
               <li>(S + s) is not a valid set</li>
          </ol>
     </li>
     <li>In case the set is valid then we further make choices and repeat the process until a solution is found, otherwise we backtrack our decision of including 's' and explore other paths until a solution is found or all the possible paths are exhausted.</li>
</ul>

</details>

<details>
<summary>PSEUDOCODE for backtracking</summary>

```python
def find_solutions(parameters):
     if valid solution:
          store the solution
          return
     for all choice:
          if valid choice:
               apply(choice)
               find_solutions(parameters)
               backtrack(remove choice)
     return
```

</details>

<details>
<summary>Complexity</summary>

Backtracking algorithm is purely brute force therefore in terms of time complexity, it performs very poorly. Generally backtracking can be seen having below mentioned time complexities:

- Exponential (O(K^N))
- Factorial (O(N!))

These complexities are due to the fact that at each state we have multiple choices due to which the number of paths increases and sub-trees expand rapidly.

</details>

<details>
<summary>Backtracking difference from Recursion</summary>

| | |
| :----: | :----: |
|Recursion|Backtracking|
|Recursion doesn't always need backtracking.|Backtracking always uses recursion to solve problems.|
|Solving problems by breaking them into smaller, similar subproblems and solving them recursively.|Solving problems with multiple choices and exploring options systematically, backtracking when needed.|
|Controlled by function calls and call stack.|Managed explicitly with loops and state.|
|Applications of Recursion: Tree and Graph Traversal, Towers of Hanoi, Divide & Conquer algorithms, Merge Sort, Quick Sort and Binary Search.|Applications of Backtracking: N Queen Problem, Rat in a Maze problem, Knight's Tour Problem, Sudoku solver, and Graph Coloring problems.|

</details>

<details>
<summary>Backtracking difference from Branch-N-Bound technique</summary>

| | | |
| :----: | :----: | :----: |
|Parameter|Backtracking|Branch-N-Bound technique|
|Approach|Backtracking is used to find all possible solutions available to a problem. When it realises that is has made a bad choice, it undoes the last choice by backing it up. It searches the state space tree until it has found a solution for the problem.|Branch-n-bound is used to solve optimisation problems. When it realises that it already has a better optimal solution that the pre-solution leads to, it abandons that pre-solution. It completely searches the state space tree to get optimal solution.|
|Traversal|Backtracking traverses the state space tree by DFS (Depth First Search) manner.|Branch-n-bound traverses the tree in any manner. DFS or BFS.|
|Function|Backtracking involves feasibility function.|Branch-n-bound involves a bounding function.|
|Problems|Backtracking is used for solving Decision Problem.|Branch-n-bound is used for solving Optimisation Problem.|
|Searching|In backtracking, the state space tree is searched until the solution is obtained.|In Branch-and-Bound as the optimum solution may be present any where in the state space tree, so the tree need to be searched completely.|
|Efficiency|Backtracking is more efficient.|Backtracking is less efficient.|
|Applications|Useful in solving N-Queen Problem, Sum of subset, Hamilton cycle problem, graph coloring problem.|Useful in solving Knapsack Problem, Travelling Salesman Problem.|
|Solve|Backtracking can solve almost any problem. (chess, sudoku, etc ).|Branch-n-bound cannot solve almost any problem.|

</details>




<h5>Exercises</h5>

|Algorithm|Description|Example|
| :----: | :----: | :----: |
|[Get all the subsets of a given array](./subsetsOfGivenArray/README.md)|Given an array Arr[] of size N, print all the subsets of the array.|Input N = 3, Arr = [1,2,3], Output: {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}|
|[Check if a string is Sum String](./sumString/README.md)|Given a string of digits, determine whether it is a 'sum-string'. A string S is called a sum-string if the rightmost substring can be written as the sum of two substrings before it and the same is recursively true for substrings before.|Input "12243660" is a sum string. Explanation: 24 + 36 = 60, 12 + 24 = 36|
|[Permutation of a given string](./permutationsString/README.md)| | |
|[Permutation of a given string within another given string](./permutationsStringToString/README.md)| | |
|[N-Queen problem]()| | |
|[Solve Sudoku]()| | |
|[M-coloring problem]()| | |
|[Rat in a Maze]()| | |
|[The Knight's Tour problem]()| | |