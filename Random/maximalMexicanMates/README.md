# Maximal Mexican Mates

- Find the size of the largest connected subgraph.

Let's consider a matrix representing a graph where 1s represent connected nodes, and 0s represent disconnected nodes. The task is to find the size of the largest connected subgraph.

<h3>Example</h3>

```
1 0 1 0 1
1 1 1 0 0
0 1 0 1 0
1 0 0 1 1
0 0 1 0 0
```

The largest connected subgraph is 11.

<h3>Considerations</h3>

- Are the values in the matrix only 1's and 0's? -> Yes
- How is the matrix structure represented? Each row from the matrix will be a line you should read from std_input, in order. You can represent it however you see fit. An array of arrays is recommended.
- It does constant amount of work each time it's called.
- At most every cell is called 10 times.