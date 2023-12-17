def allConstruct(target, wordBank):
     
     if target == '':
          return [[]]
     
     result = []

     for word in wordBank:
          if target.startswith(word):
               suffix = target[len(word):]
               suffixWays = allConstruct(suffix, wordBank)
               targetWays = [[word, *way] for way in suffixWays]
               result.extend(targetWays)

     return result

     
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('hello', ['cat', 'dog', 'mouse']))
print(allConstruct('', ['cat', 'dog', 'mouse']))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa']))

print()

def allConstruct(target, wordBank, memo = {}):
     if target in memo:
          return memo[target]
     
     if target == '':
          return [[]]
     
     result = []

     for word in wordBank:
          if target.startswith(word):
               suffix = target[len(word):]
               suffixWays = allConstruct(suffix, wordBank)
               targetWays = [[word, *way] for way in suffixWays]
               result.extend(targetWays)

     memo[target] = result
     return result

     
print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('hello', ['cat', 'dog', 'mouse']))
print(allConstruct('', ['cat', 'dog', 'mouse']))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']))