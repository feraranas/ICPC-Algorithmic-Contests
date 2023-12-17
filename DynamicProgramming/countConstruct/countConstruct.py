def countConstruct(target, wordBank):
     if target == '':
          return 1
     
     totalCount = 0

     for word in wordBank:
          if target.startswith(word):
               # number of ways we can generate the suffix with the rest of the target
               numWaysForRest = countConstruct(target[len(word):], wordBank)
               totalCount += numWaysForRest
     
     return totalCount



print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'ot', 'o', 't']))

print()

def countConstructMemoized(target, wordBank, memo = {}):
     if target in memo:
          return memo[target]
     if target == '':
          return 1
     
     totalCount = 0

     for word in wordBank:
          if target.startswith(word):
               # number of ways we can generate the suffix with the rest of the target
               numWaysForRest = countConstructMemoized(target[len(word):], wordBank, memo)
               totalCount += numWaysForRest
     
     memo[target] = totalCount
     return totalCount

print(countConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False