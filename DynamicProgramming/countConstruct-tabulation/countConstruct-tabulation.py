def countConstructTabulation(target, wordBank):
     
     table = [0] * (len(target) + 1)
     
     table[0] = 1

     for i in range(len(table)):
          for word in wordBank:
               if target[i:i+len(word)] == word:
                    table[i + len(word)] += table[i]

     return table[len(target)]

print(countConstructTabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstructTabulation('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstructTabulation('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstructTabulation('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
