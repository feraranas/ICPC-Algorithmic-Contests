/*
Write a function `bestSum(targetSum, numbers)`that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.

If there's a tie for the shortestCombination, you may return any one of the shortest.
bestSum(7, [5,3,4,7]) : [3,4] , [7] -> [7]
bestSum(8, [2,3,5]) : [2, 2, 2], [2, 3, 3], [3, 5] -> [8]
*/

const bestSum = (targetSum, numbers) => {
     if (targetSum === 0) return [];
     if (targetSUm < 0) return null;

     let shortestCombination = null;

     for (let n of numbers) {
          const rem = targetSum - n;
          const res = bestSum(rem, numbers);
          if (res !== null) {
               const combination = [...res, n];
               // if the combination is shorter than the current "shortest", update it
               if (shortestCombination === null || combination.length < shortestCombination.length){ 
                    shortestCombination = combination;
               }
          }
     }

     return shortestCombination;
}

console.log(bestSum(7, [5,3,4,7])); // [7]
console.log(bestSum(8, [2,3,5])); // [3,5]
console.log(bestSum(8, [1,4,5])); // [4,4]
console.log(bestSum(100, [1,2,5,25])); // [25,25,25,25]