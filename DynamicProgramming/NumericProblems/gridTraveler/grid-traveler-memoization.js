/*
 So dynamic programming it's all about identifying similar patterns in a tree.
 A tree is proposed every-time we make recursive calls. We think of recursive functions
 in terms of a tree.

 Example : gridTraveler(4,3)
                    (m,n)          m : {0,1,2,3,4}
               /              \
          ()                       n : {0,1,2,3}

          So m * n possible combinations

Brute Force              |    Memoized
O(2 ^ (n + m)) time      |    O(n * m)
O(n + m) space           |    O(n + m) space
*/

const gridTraveler = (n, m, memo = {}) => {
     const key = n + ',' + m;
     if (key in memo) return memo[key];
     if (m === 1 && n === 1) return 1;
     if (m === 0 || n === 0) return 0;
     memo[key] = gridTraveler(n - 1, m, memo) + gridTraveler(n, m - 1, memo);
     return memo[key];
}

console.log(gridTraveler(18,18));