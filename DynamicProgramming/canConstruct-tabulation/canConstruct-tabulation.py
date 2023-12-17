def canConstructTabulation(target, wordBank):
     table = [False] * (len(target) + 1)
      
     table[0] = True

     for i in range(len(table)):
          if table[i] == True:
                for word in wordBank:
                     if target[i : i + len(word)] == word:
                          table[i + len(word)] = True

     return table[len(target)]


print(canConstructTabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstructTabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstructTabulation("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
print(canConstructTabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
