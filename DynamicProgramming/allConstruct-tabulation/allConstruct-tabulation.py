def allConstructTabulation(target, wordBank):
     table = [[] for _ in range(len(target) + 1)]
     table[0] = [[]]

     for i in range(len(target)):
          for word in wordBank:
               if target[i: i + len(word)] == word:
                    newCombinations = [[*subarray, word] for subarray in table[i]]
                    table[i + len(word)].extend(newCombinations)

     return table[len(target)]


print(allConstructTabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstructTabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstructTabulation('hello', ['cat', 'dog', 'mouse']))
print(allConstructTabulation('', ['cat', 'dog', 'mouse']))
# print(allConstructTabulation('aaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa']))