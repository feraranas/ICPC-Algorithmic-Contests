# Best Sum Tabulated

<h2>Description</h2>

Write a function ```bestSumTabulation(targetSum, numbers)``` that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.

If there's a tie for the shortest combination, you may return any one of the shortest.

<h2>Example</h2>

```bestSumTabulation(8, [2,3,5]) -> [[2,2,2,2], [3,3,2], [3,5]] => R: [3,5]```

Start by assigning the base case

<img width=400px src="./assets/ex1.png">

<img width=400px src="./assets/ex2.png">

<img width=400px src="./assets/ex3.png">

<img width=400px src="./assets/ex4.png">

<img width=400px src="./assets/ex5.png">

here, we have an overlap of arrays that can generate '5', so we choose the shortest array from both, in this case [5]

<img width=400px src="./assets/ex6.png">

<img width=400px src="./assets/ex7.png">

<img width=400px src="./assets/ex8.png">

<img width=400px src="./assets/ex9.png">

<img width=400px src="./assets/ex10.png">

<img width=400px src="./assets/ex11.png">

<img width=400px src="./assets/ex12.png">

<img width=400px src="./assets/ex13.png">

<img width=400px src="./assets/ex14.png">

<img width=400px src="./assets/ex15.png">

<img width=400px src="./assets/ex16.png">

<img width=400px src="./assets/ex17.png">

<img width=400px src="./assets/
ex18.png">

## Complexity

<img width=400px src="./assets/ex18.png">