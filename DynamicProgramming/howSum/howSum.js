/**
 * Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.
 * The function should return an array, containing any combination of elements that add up to exactly the targetSum.
 * If there is no combination that adds up to the targetSum, then return null.
 * 
 * If there are multiple combinations possible, you may return any option.
 * howSum(7, [5,3,4,7]) -> [3, 4], [7]
 * howSum(7, [2, 4]) -> null
 * howSum(8, [2,3,5]) -> [2,2,2,2], [5,3]
 * howSum(8, [10,3,1,7,5]) -> [3,3,1,1]
 * howSum(0, [1,2,3]) -> []
 */

const howSum = (targetSum, numbers) => {
     if (targetSum === 0) return [];
     if (targetSum < 0) return null;
     for (let n of numbers) {
          const rem = targetSum - n;
          const remRes = howSum(rem, numbers);
          if (remRes !== null) {
               return [ ...remRes, n ];
          }
     }
     return null;
}


console.log(howSum(7, [5,3,4,7]))
console.log(howSum(7, [2, 4]))
console.log(howSum(8, [2,3,5]))
console.log(howSum(8, [10,3,1,7,5]))
console.log(howSum(0, [1,2,3]))