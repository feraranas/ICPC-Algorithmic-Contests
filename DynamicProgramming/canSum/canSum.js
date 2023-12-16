/*
Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments. The function should return a boolean indicating whether or not
it is possible to generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.
You may assume that all input numbers are nonnegative.

canSum(7, [5,3,4,7]) -> true
canSum(7, [2,4]) -> false

                              7
               /(-5)     |(-3)          |(-4)     \(-7)
               2         4              3            0
                      /(-3) \(-4)       |(-3)
                    1        0         0
          
The base case is 0, which returns 'true'
*/

const canSum = (targetSum, numbers) => {
     if (targetSum === 0) return true;
     if (targetSum < 0) return false; 
     for (let num of numbers) {
          const rem = targetSum - num;
          if (canSum(rem, numbers) === true) {
               return true;
          }
     }
     return false;
}

console.log(canSum(6, [2, 3, 4]));