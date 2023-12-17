/* Using memoization

In how many ways can you travel to the goal on a grid with dimensions m * n
You begin in the top-left corner and your goal is travel to the bottom-right corner. 
You may only move down or right.

gridTraveler(1,1) -> 1 'do nothing'
gridTraveler(0,1) -> 0 ?
gridTraveler(1,0) -> 0 ?
gridTraveler(0,0) -> 0 ?

Try to decrease the problem size in each iteration.
If we have a problem that behaves recursivelly, formalize it as a Tree.
                 (2,3)
               /       \
          (1,3)          (2,2)
         /    \          /     \
     (0,3)   (1,2)     (1,2)     (2,1)
             /   \      /   \     /   \
         (0,2) (1,1) (0,2) (1,1) (1,1) (2,0)

O(2^(n+m)) time
O(n + m) space
*/
const gridTraveler = (n, m) => {
     if (m === 1 && n === 1) return 1;
     if (m === 0 || n === 0) return 0;
     return gridTraveler(n - 1, m) + gridTraveler(n, m - 1);
}

console.log(gridTraveler(3,3));