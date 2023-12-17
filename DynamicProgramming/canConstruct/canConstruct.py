def canConstruct(target, wordBank):
     if target == '':
          return True
     
     for word in wordBank:
          if target.startswith(word):
               suffix = target[len(word):]
               if canConstruct(suffix, wordBank):
                    return True
     
     return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))

print()
print()
print()

def canConstructMemoized(target, wordBank, memo = {}):
     if target in memo:
          return memo[target]
     if target == '':
          return True
     
     for word in wordBank:
          if target.startswith(word):
               suffix = target[len(word):]
               if canConstructMemoized(suffix, wordBank, memo):
                    memo[target] = True
                    return True
     
     memo[target] = False
     return False

print(canConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False