class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cToStr, strSet, s = {}, set(), s.split(' ')
        if len(s) != len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] in cToStr:
                if cToStr[pattern[i]] != s[i]: return False
            elif s[i] in strSet: return False
            else:
                cToStr[pattern[i]] = s[i]
                strSet.add(s[i])
        return True
        
