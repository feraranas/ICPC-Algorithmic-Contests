from collections import Counter
# from sortedString import sortingString

class Solution:
    # runtme: 89ms, memory: 17.7mb
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)
        if len(cs) != len(ct):
            return False
        for i, v in cs.items():
            if ct[i] != v:
                return False
        return True
    
    # runtme: 69ms, memory: 17.9mb
    def isAnagram2(self, s: str, t: str) -> bool:
        cs = dict()
        ct = dict()
        if len(s) != len(t):
            return False
        
        for c1, c2 in zip(s, t):
            if c1 not in cs:
                cs[c1] = 1
            else:
                cs[c1] += 1
            if c2 not in ct:
                ct[c2] = 1
            else:
                ct[c2] += 1
        
        for i in set(cs.keys()):
            try:
                if ct[i] != cs[i]:
                    return False
            except:
                return False
    
        return True
    
    # runtme: 52ms, memory: 18.2mb
    def isAnagram3(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram4(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            a='abcdefghijklmnopqrstuvwxyz'
            for i in a:
                if s.count(i)!=t.count(i):
                    return False
        return True
    
    
print(sorted("anagram"))
    
