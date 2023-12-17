# Can Construct Tabulated

<h2>Description</h2>

Write a function ```canConstruct(target, wordBank)``` that accepts a target string and an array of strings.

The function should return a boolean indicating whether or not the ```target``` can be constructed by concatenating elements of the ```wordBank``` array.

You may reuse elements of ```wordBank``` as many times as needed.

<h2>Example</h2>

```canConstruct(abcdef, [ab, abc, cd, def, abcd])``` -> True "abc" + "def"

<img width=400px src="./assets/ex1.png">

What's the point of the ending spot?

We need a way to represent information about the empty string.

Here's the pattern:

If we look at index 0 of this table, we are making a statement about the empty string. So if we look at a spot in this table, depending on what that index is we are considering the substring that starts at index 0 and goes up to but not including the current position. 

<img width=400px src="./assets/ex2.png">

<img width=400px src="./assets/ex3.png">

<img width=400px src="./assets/ex4.png">

<img width=400px src="./assets/ex5.png">

<img width=400px src="./assets/ex6.png">

<img width=400px src="./assets/ex7.png">

<img width=400px src="./assets/ex8.png">

The base case is:

<img width=400px src="./assets/ex9.png">

<img width=400px src="./assets/ex10.png">

<img width=400px src="./assets/ex11.png">

<img width=400px src="./assets/ex12.png">

<img width=400px src="./assets/ex13.png">

<img width=400px src="./assets/ex14.png">

<img width=400px src="./assets/ex15.png">

Here, it's not possible to generate the word **a**.

<img width=400px src="./assets/ex16.png">

<img width=400px src="./assets/ex17.png">

<img width=400px src="./assets/ex18.png">

<img width=400px src="./assets/ex19.png">

<img width=400px src="./assets/ex20.png">

<img width=400px src="./assets/ex21.png">

<img width=400px src="./assets/ex22.png">

<img width=400px src="./assets/ex23.png">

## Complexity

<img width=400px src="./assets/ex24.png">