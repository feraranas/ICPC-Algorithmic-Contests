function canConstruct(target, wordBank, memo = {}) {
     if (target in memo) {return memo[target]}
     if (target === '') {
          return true
     }
     for (let word of wordBank) {
          if (target.indexOf(word) === 0) {
               const suffix = target.slice(word.length)
               if (canConstruct(suffix, wordBank, memo) === true) {
                    memo[target] = true;
                    return true;
               }
          }
     }
     memo[target] = false;
     return false;
}

console.log(canConstruct('abcdef', ['ab','abc','cd','def','abcd']))
console.log(canConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
console.log(canConstruct('', ['cat','dog','snake']))
console.log(canConstruct('fernando', ['F','e','r','n','a','n','d','o']))
console.log(canConstruct('fernando', ['f','e','r','n','a','n','d','o']))