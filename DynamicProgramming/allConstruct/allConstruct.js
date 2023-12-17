function allConstruct(target, wordBank) {
    if (target === '') {return []}  
    let lst = []
    for (let word of wordBank) {
     if (target.indexOf(word) === 0) {
        let suffix = target.slice(word.length)
          if (allConstruct(suffix, wordBank) === true) {
            lst.push(suffix)
            return lst
          }
     }
    }
    return lst
}

console.log(allConstruct('abcdef', ['ab','abc','cd','def','abcd']))
console.log(allConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))
console.log(allConstruct('', ['cat','dog','snake']))
console.log(allConstruct('fernando', ['F','e','r','n','a','n','d','o']))
console.log(allConstruct('fernando', ['f','e','r','n','a','n','d','o']))