/**
 * m = target sum
 * n = numbers.length
 * 
 * Brute Force
 * time : O(n^m * m)
 * space : O(m)
 * 
 * Memoized
 * time : O(n*m^2)
 * space : O(m)
 */

const howSum = (targetSum, numbers, memo={}) => {
     if (targetSum in memo) return memo[targetSum];
     if (targetSum === 0) return [];
     if (targetSum < 0) return null;
     for (let n of numbers) {
          const rem = targetSum - n;
          const remRes = howSum(rem, numbers, memo);
          if (remRes !== null) {
               memo[targetSum] = [...remRes, n];
               return memo[targetSum];
          }
     }
     memo[targetSum] = null;
     return null;
}

console.log(howSum(7, [5,3,4,7]))
console.log(howSum(7, [2, 4]))
console.log(howSum(8, [2,3,5]))
console.log(howSum(8, [10,3,1,7,5]))
console.log(howSum(0, [1,2,3]))
console.log(howSum(300, [7,14]))