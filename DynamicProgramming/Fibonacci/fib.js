/* MEMOIZATION RECIPE:

1. Make it work (brute force). (Look for correctness)
     -> Visualize the problem as a tree.
     -> Visualize smaller instances of the problem (shrink the size of the
problem).
     -> Implement the tree using recursion.
          -> Finding the base(s) case(s)
     -> Test it.

2. Make it efficient.
     -> Add a memo object. (Key's and Argument (return values)).
     -> Add a new base case to return memo values.
     -> Store return values into the memo.

1. & 2
*/

/* Fibonacci
O(2^n) time
O(n) space
*/

const fib =
    (n) => {
      if (n <= 2)
        return 1;
      return fib(n - 1) + fib(n - 2);
    }

           console.log(fib(13));