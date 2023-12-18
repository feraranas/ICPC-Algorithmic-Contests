# Count Construct Tabulated

<h2>Description</h2>

Write a function ```countConstruct(target, wordBank)``` that accepts a target string and an array of strings.

The function should return the number of ways that the ```target``` can be constructed by concatenating elements of the ```worldBank``` array.

You may reuse elements of ```wordBank``` as many times as needed.

<h2>Example</h2>

```countConstruct(purple, [purp, p, ur, le, purpl]) -> 2```

<img width=350px src="./assets/ex1.png">

Base case is:

<img width=350px src="./assets/ex2.png">

<img width=350px src="./assets/ex3.png">

Start all other slots at zero.

<img width=350px src="./assets/ex4.png">

When we are at some position, we go up to but not including that.

So from any position, we should consider any other spot within the table. So, in index 0, we consider words that start with **p**.

<img width=350px src="./assets/ex5.png">

<img width=350px src="./assets/ex6.png">

<img width=350px src="./assets/ex7.png">

<img width=350px src="./assets/ex8.png">

This was the very first pass, now we move current position to the right.

<img width=350px src="./assets/ex9.png">

Next spot, Nothing happens. We progress.

<img width=350px src="./assets/ex10.png">

<img width=350px src="./assets/ex11.png">

<img width=350px src="./assets/ex12.png">

<img width=350px src="./assets/ex13.png">

<img width=350px src="./assets/ex14.png">

<img width=350px src="./assets/ex15.png">

Now, we see that looking into index 4, we see a 2. We are considering a substring that starts at 0 up to but not including 4. If there's a 2, there's 2 ways to generate **purp**.

<img width=350px src="./assets/ex16.png">

We could have taken **+le**. 

<img width=350px src="./assets/ex17.png">

<img width=350px src="./assets/ex18.png">

## Complexity

<img width=350px src="./assets/ex19.png">