const bestSum = (targetSum, numbers, memo={}) => {
     if (targetSum in memo) return memo[targetSum];
     if (targetSum === 0) return [];
     if (targetSum < 0) return null;

     let shortestCombination = null;

     for (let n of numbers) {
          const rem = targetSum - n;
          const res = bestSum(rem, numbers, memo);
          if (res !== null) {
               const combination = [...res, n];
               if (shortestCombination === null || combination.length < shortestCombination.length) {
                    shortestCombination = combination;
               }
          }
     }

     memo[targetSum] = shortestCombination;
     return shortestCombination;
}

console.log(bestSum(100, [1,2,5,25]));