/* ////////////// */
/* /// RESULT /// */
/* ////////////// */

function canConstruct(target, wordBank) {
     if (target === '') {
          return true
     }
     for (let word of wordBank) {
          if (target.indexOf(word) === 0) {
               const suffix = target.slice(word.length)
               if (canConstruct(suffix, wordBank) === true) {
                    return true;
               }
          }
     }
     return false;
}

/* ////////////// */
/* // FIRST TRY //*/
/* ////////////// */
/*
function isInArray(n, Array){
     if (Array.length <= 1) {
          return Array[0] === n ? true : false
     }
     for (let m of Array) {
          if (n === m) return true
     }
     return false
}

function canConstruct(target, Array) {
     if (target.length === 0) {
          return false
     }
     const aNew = target.slice(0, target.length / 2);
     let isAnew = isInArray(aNew, Array) ? true : false;
     const bNew = target.slice(target.length / 2, target.length)
     let isBnew = isInArray(bNew, Array) ? true : false;
     if (isAnew && isBnew) {
          return true
     }
     else if (!isAnew && !isBnew){
          return canConstruct(aNew, Array) && canConstruct(bNew, Array)
     }
     else if (!isAnew && isBnew){
          return canConstruct(aNew, Array)
     }
     else if (isAnew && !isBnew){
          return canConstruct(bNew, Array)
     }
}
*/

console.log(canConstruct('abcdef', ['ab','abc','cd','def','abcd']))
console.log(canConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
console.log(canConstruct('', ['cat','dog','snake']))
console.log(canConstruct('fernando', ['F','e','r','n','a','n','d','o']))
console.log(canConstruct('fernando', ['f','e','r','n','a','n','d','o']))